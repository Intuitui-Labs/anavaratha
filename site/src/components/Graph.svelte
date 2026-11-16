<script lang="ts">
  import { onMount } from 'svelte';
  let { data } = $props();
  const presets: Record<string, { label: string; kinds: string[] }> = {
    lineage: { label: 'Lineage · legacy → current', kinds: ['doc', 'legacy_concept', 'current_object', 'frame', 'domain', 'root'] },
    institutions: { label: 'Institutions · responsibility chain', kinds: ['institution', 'chain_link'] },
    projects: { label: 'Projects · funders & implementers', kinds: ['project', 'org'] },
    concepts: { label: 'Concepts · domains, frames, grammar', kinds: ['root', 'domain', 'frame', 'glossary', 'shared_grammar'] },
  };
  const relColor: Record<string, string> = { DUP: '#c2410c', 'DUP+CON': '#b45309', CON: '#b91c1c', EXT: '#15803d', IGN: '#94a3b8', NEW: '#0369a1' };
  const kindColor: Record<string, string> = { root: '#090d16', domain: '#15803d', frame: '#0369a1', glossary: '#7dd3fc', shared_grammar: '#86efac', legacy_concept: '#fdba74', current_object: '#bae6fd', doc: '#e2e8f0', institution: '#ffffff', chain_link: '#090d16', compliance_step: '#334155', project: '#fecaca', org: '#fde68a' };
  let preset = $state('lineage');
  let sel: any = $state(null);
  let el: HTMLDivElement;
  let cy: any;
  const byId = new Map(data.nodes.map((n: any) => [n.id, n]));
  const ALWAYS = new Set(['root', 'domain', 'frame', 'chain_link', 'org', 'institution']);
  const HUBS = 12; // labelled at any zoom: top-degree nodes in the view + structural kinds
  function elements(p: string) {
    const ks = new Set(presets[p].kinds);
    const ns = data.nodes.filter((n: any) => ks.has(n.kind));
    const ids = new Set(ns.map((n: any) => n.id));
    const es = data.edges.filter((e: any) => ids.has(e.source) && ids.has(e.target));
    const deg = new Map<string, number>();
    for (const e of es) { deg.set(e.source, (deg.get(e.source) ?? 0) + 1); deg.set(e.target, (deg.get(e.target) ?? 0) + 1); }
    const top = new Set([...deg.entries()].sort((a, b) => b[1] - a[1]).slice(0, HUBS).map(([k]) => k));
    return [
      ...ns.map((n: any) => ({ data: { id: n.id, label: n.label.length > 42 ? n.label.slice(0, 40) + '…' : n.label, kind: n.kind, color: kindColor[n.kind] ?? '#fff', pat: n.pattern ? n.pattern[0] : '', deg: deg.get(n.id) ?? 0 }, classes: top.has(n.id) || ALWAYS.has(n.kind) ? 'hub' : '' })),
      ...es.map((e: any, i: number) => ({ data: { id: `e${i}-${e.source}-${e.target}`, source: e.source, target: e.target, rel: e.rel, label: e.keyword ? `“${e.keyword}”?` : (relColor[e.rel] ? e.rel : ''), color: e.rel === 'role_keyword' ? '#64748b' : relColor[e.rel] ?? '#94a3b8' } })),
    ];
  }
  // Labels keep a constant on-screen size; below FULL zoom only hubs are labelled.
  const FULL = 0.85;
  function relabel() {
    if (!cy) return;
    const z = cy.zoom(); const fs = Math.min(36, 12.5 / z);
    cy.batch(() => {
      cy.nodes().forEach((n: any) => n.toggleClass('lbl', z >= FULL || n.hasClass('hub') || n.selected()));
      cy.edges().forEach((e: any) => e.toggleClass('lbl', z >= FULL * 1.2 || e.data('rel') === 'role_keyword'));
    });
    cy.style([...baseStyle, { selector: 'node.lbl', style: { 'font-size': fs, 'text-max-width': `${Math.round(170 / Math.max(z, 0.2))}px` } }, { selector: 'edge.lbl', style: { 'font-size': Math.min(28, 10 / z) } }]);
  }
  let raf = 0;
  const onZoom = () => { cancelAnimationFrame(raf); raf = requestAnimationFrame(relabel); };
  function focusNode(id: string) {
    if (!cy) return; const n = cy.getElementById(id); if (!n || n.empty()) return;
    cy.$(':selected').unselect(); n.select(); sel = byId.get(id);
    const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
    reduce ? cy.center(n) : cy.animate({ center: { eles: n }, duration: 250 });
    relabel();
  }
  const chainOrder = ['ch_duty', 'ch_capacity', 'ch_detection', 'ch_enforcement', 'ch_remedy', 'ch_persistence'];
  function positions(p: string): Record<string, { x: number; y: number }> | null {
    const ks = new Set(presets[p].kinds); const ns = data.nodes.filter((n: any) => ks.has(n.kind)); const pos: Record<string, { x: number; y: number }> = {};
    if (p === 'institutions') {
      ns.filter((n: any) => n.kind === 'institution').forEach((n: any, i: number) => (pos[n.id] = { x: i * 125, y: (i % 3) * 95 }));
      chainOrder.forEach((id, i) => (pos[id] = { x: 20 + i * 250, y: 560 }));
      return pos;
    }
    if (p === 'lineage') {
      const col: Record<string, number> = { doc: 0, legacy_concept: 1, current_object: 2, frame: 3, domain: 3, root: 3 };
      const counts = [0, 0, 0, 0];
      const order = [...ns].sort((a: any, b: any) => (a.date ?? '').localeCompare(b.date ?? ''));
      for (const n of order) { const c = col[n.kind]; pos[n.id] = { x: c * 420, y: counts[c]++ * (c === 0 ? 120 : c === 3 ? 150 : 52) }; }
      return pos;
    }
    return null;
  }
  function layoutFor(p: string) {
    const pos = positions(p);
    return pos ? { name: 'preset', positions: (n: any) => pos[n.id()] ?? { x: 0, y: 0 }, fit: true, padding: 70 } : { name: 'cose', animate: false, nodeRepulsion: () => 9000, idealEdgeLength: () => 90, padding: 20, randomize: false };
  }
  const baseStyle: any[] = [
        { selector: 'node', style: { label: '', 'background-color': 'data(color)', 'border-width': 1, 'border-color': '#334155', 'font-size': 13, 'text-wrap': 'wrap', 'text-max-width': '150px', 'text-valign': 'bottom', 'text-margin-y': 3, 'min-zoomed-font-size': 0, width: 16, height: 16, color: '#090d16' } },
        { selector: 'node[kind = "chain_link"], node[kind = "root"]', style: { color: '#090d16', 'font-weight': 'bold', width: 26, height: 26 } },
        { selector: 'node[kind = "institution"]', style: { shape: 'round-rectangle', width: 22, height: 14 } },
        { selector: 'node[pat = "a"]', style: { 'background-color': '#f87171' } },
        { selector: 'node[pat = "b"]', style: { 'background-color': '#4ade80' } },
        { selector: 'node.lbl', style: { label: 'data(label)' } },
        { selector: 'edge', style: { width: 1.4, 'line-color': 'data(color)', 'target-arrow-color': 'data(color)', 'target-arrow-shape': 'triangle', 'curve-style': 'bezier', label: '', 'font-size': 10, color: '#334155', 'text-background-color': '#fff', 'text-background-opacity': 0.85 } },
        { selector: 'edge.lbl', style: { label: 'data(label)' } },
        { selector: 'edge[rel = "IGN"]', style: { 'line-style': 'dashed' } },
        { selector: 'edge[rel = "role_keyword"]', style: { 'line-style': 'dashed', 'line-dash-pattern': [5, 4], width: 1.2, 'target-arrow-shape': 'none', 'font-style': 'italic', color: '#475569' } },
        { selector: 'edge.lbl[rel = "role_keyword"]', style: { 'text-rotation': 'autorotate', 'text-background-opacity': 0.9 } },
        { selector: ':selected', style: { 'border-width': 3, 'border-color': '#0369a1' } },
      ];
  async function draw() {
    const cytoscape = (await import('cytoscape')).default;
    cy?.destroy();
    cy = cytoscape({
      container: el, elements: elements(preset), wheelSensitivity: 0.3,
      style: baseStyle,
      layout: layoutFor(preset),
    });
    cy.on('tap', 'node', (e: any) => { sel = byId.get(e.target.id()); });
    cy.on('zoom', onZoom); relabel();
    cy.on('tap', 'edge', (e: any) => { const d = data.edges.find((x: any) => x.source === e.target.data('source') && x.target === e.target.data('target') && x.rel === e.target.data('rel')); sel = d ? { label: `${d.source} → ${d.target}`, kind: 'edge · ' + d.rel, src: d.src, keyword: d.keyword } : null; });
  }
  onMount(() => () => cy?.destroy());
  $effect(() => { preset; if (el) draw(); });
  const visible = $derived(data.nodes.filter((n: any) => presets[preset].kinds.includes(n.kind)));
  let q = $state('');
  const found = $derived(q.length < 2 ? [] : visible.filter((n: any) => n.label.toLowerCase().includes(q.toLowerCase())).slice(0, 8));
</script>

<div class="space-y-3">
  <div role="radiogroup" aria-label="Graph view" class="flex flex-wrap gap-2">
    {#each Object.entries(presets) as [k, p]}
      <button role="radio" aria-checked={preset === k} class={`chip ${preset === k ? '!bg-brand-primary !text-white' : ''}`} onclick={() => { preset = k; sel = null; }}>{p.label}</button>
    {/each}
  </div>
  <div class="flex flex-wrap gap-3 text-xs font-mono">
    {#each Object.entries(relColor) as [r, c]}<span><span style="color:{c}">━</span> {r}</span>{/each}
    <span class="text-brand-muted">DUP redo · EXT beyond · CON conflicts with lock · IGN ignored</span>
  </div>
  {#if preset === 'institutions'}
    <p class="panel !py-2 text-sm border-l-4 !border-l-slate-500"><strong>Dashed grey links are keyword matches, not judgements.</strong> An actor links to a chain step when its formal-role text contains a word such as “inspect” or “prosecute”. The label shows the matched word with a “?”. Nothing here says the actor does, or fails to do, that step.</p>
  {/if}
  <label class="text-sm flex flex-wrap items-center gap-2">Find a node <input bind:value={q} class="chip !py-1 font-mono" placeholder="type 2+ letters" aria-describedby="find-hint" />
    <span id="find-hint" class="text-xs text-brand-muted">Tab to a result, then Enter. The graph centres on it. Zoom in to see every label; zoomed out, only the {HUBS} most-connected nodes and the structural ones are labelled.</span></label>
  {#if found.length}<ul class="flex flex-wrap gap-2 text-sm">{#each found as n}<li><button class="chip" onclick={() => focusNode(n.id)}>{n.label}</button></li>{/each}</ul>{/if}
  <div class="grid lg:grid-cols-[1fr_300px] gap-4">
    <div bind:this={el} class="panel !p-0 h-[560px]" role="img" aria-label={`Relationship graph, view: ${presets[preset].label}. ${visible.length} nodes. A text list follows.`}></div>
    <aside class="panel text-sm space-y-2" aria-live="polite">
      {#if sel}
        <p class="mono-label">{sel.kind}</p><p class="font-bold">{sel.label}</p>
        {#if sel.question}<p>Q: {sel.question}</p>{/if}
        {#if sel.role}<p><strong>Formal role:</strong> {sel.role}</p><p><strong>Capacity that must exist:</strong> {sel.capacity_needed}</p><p><strong>Evidence to seek:</strong> {sel.evidence_to_seek}</p>{/if}
        {#if sel.legacy_source}<p><strong>Legacy source:</strong> {sel.legacy_source}</p>{/if}
        {#if sel.years_text}<p><strong>Years:</strong> {sel.years_text} · pattern {sel.pattern}</p>{/if}
        {#if sel.keyword}<p><strong>Role keyword:</strong> “{sel.keyword}”</p><p class="text-xs text-brand-muted">Inferred: this word appears in the actor's formal-role text. Not a judgement of practice.</p>{/if}
        <p class="src">src: {sel.src}</p>
      {:else}<p class="text-brand-muted">Tap a node or edge. Drag to rearrange; scroll to zoom.</p>{/if}
    </aside>
  </div>
  <details class="text-sm"><summary class="cursor-pointer font-semibold">Text list of the {visible.length} nodes in this view</summary>
    <ul class="columns-2 mt-2">{#each visible as n}<li><button class="text-left underline decoration-dotted hover:decoration-solid" onclick={() => focusNode(n.id)}>{n.label}</button> <span class="src">({n.kind})</span></li>{/each}</ul>
  </details>
</div>
