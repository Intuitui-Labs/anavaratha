<script lang="ts">
  import { scaleTime, scaleLinear } from 'd3-scale';
  let { data } = $props();
  const typeColor: Record<string, string> = { first: '#0369a1', mutation: '#c2410c', accretion: '#15803d', rename: '#7c3aed', drop: '#b91c1c', dormant: '#64748b', revival: '#0891b2' };
  const patColor: Record<string, string> = { a: '#b91c1c', b: '#15803d', c: '#64748b' };
  let w = $state(900);
  let show = $state({ a: true, b: true, c: true });
  let sel: any = $state(null);
  let asTable = $state(false);
  const types = Object.keys(typeColor);
  const ev = data.concept_events;
  // events sharing date + kind are nudged apart (8 px each) so none hides another
  const nudge = (() => { const seen = new Map<string, number>(); return ev.map((e: any) => { const k = e.date + e.type; const n = seen.get(k) ?? 0; seen.set(k, n + 1); return n * 8; }); })();
  const x1 = $derived(scaleTime().domain([new Date('2026-02-01'), new Date('2026-11-30')]).range([110, w - 20]));
  const rowY = (t: string) => 30 + types.indexOf(t) * 26;
  const projs = $derived(data.projects.filter((p: any) => p.start && show[p.pattern[0] as 'a' | 'b' | 'c']).sort((a: any, b: any) => a.pattern.localeCompare(b.pattern) || a.start - b.start));
  const x2 = $derived(scaleLinear().domain([1994, 2030]).range([60, w - 20]));
  const undated = $derived(data.projects.filter((p: any) => !p.start && show[p.pattern[0] as 'a' | 'b' | 'c']));
  const months = ['2026-02-01','2026-03-01','2026-04-01','2026-05-01','2026-06-01','2026-07-01','2026-08-01','2026-09-01','2026-10-01','2026-11-01'];
  function pick(o: any) { sel = o; }
  function key(e: KeyboardEvent, o: any) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); pick(o); } }
</script>

<div class="space-y-6">
  <div class="flex flex-wrap items-center gap-3 text-sm">
    <button class="chip" onclick={() => (asTable = !asTable)} aria-pressed={asTable}>{asTable ? 'Show chart' : 'Show as table'}</button>
    <span class="mono-label">Ledger pattern:</span>
    {#each ['a', 'b', 'c'] as p}
      <label class="chip cursor-pointer"><input type="checkbox" bind:checked={show[p as 'a'|'b'|'c']} /> <span style="color:{patColor[p]}">■</span> {p} · {data.meta.pattern_key[p]}</label>
    {/each}
  </div>

  {#if asTable}
    <table class="w-full text-sm border-collapse">
      <caption class="text-left font-bold mb-2">Concept events (CHRONOLOGY §A) and ledger rows</caption>
      <thead><tr class="text-left border-b"><th>Date / years</th><th>Kind</th><th>Item</th><th>Source</th></tr></thead>
      <tbody>
        {#each ev as e}<tr class="border-b align-top"><td class="font-mono">{e.date}</td><td>{e.type}</td><td><strong>{e.title}</strong> — {e.effect}</td><td class="src">{e.src}</td></tr>{/each}
        {#each [...projs, ...undated] as p}<tr class="border-b align-top"><td class="font-mono">{p.years_text}</td><td>pattern {p.pattern}</td><td><strong>{p.id}</strong> {p.name}</td><td class="src">{p.src}</td></tr>{/each}
      </tbody>
    </table>
  {:else}
  <figure bind:clientWidth={w} class="panel">
    <figcaption class="font-bold">Ideas, Feb → Nov 2026 <span class="text-brand-muted font-normal text-sm">· accretion, mutation, rename, drop, revival</span></figcaption>
    <svg width={w - 40} height={30 + types.length * 26 + 20} role="img" aria-label="Concept event timeline February to November 2026">
      {#each months as m}
        <line x1={x1(new Date(m))} x2={x1(new Date(m))} y1="18" y2={30 + types.length * 26} stroke="#e2e8f0" />
        <text x={x1(new Date(m)) + 3} y="12" font-size="10" fill="#334155">{new Date(m).toLocaleString('en', { month: 'short' })}</text>
      {/each}
      <rect x={x1(new Date('2026-02-25'))} width={x1(new Date('2026-08-22')) - x1(new Date('2026-02-25'))} y="18" height={types.length * 26 + 6} fill="#f1f5f9" />
      <text x={x1(new Date('2026-05-10'))} y={30 + types.length * 13} font-size="11" fill="#64748b" text-anchor="middle">dormant ~6 months</text>
      {#each types as t}<text x="0" y={rowY(t) + 4} font-size="11" font-family="var(--font-mono)" fill={typeColor[t]}>{t}</text>{/each}
      {#each ev as e, i}
        <g role="button" tabindex="0" aria-label={`${e.date} ${e.type}: ${e.title}`} onclick={() => pick(e)} onkeydown={(k) => key(k, e)} style="cursor:pointer">
          <circle cx={x1(new Date(e.date)) + nudge[i]} cy={rowY(e.type)} r={sel === e ? 9 : 6.5} fill={typeColor[e.type]} stroke="#fff" stroke-width="2" />
        </g>
      {/each}
    </svg>
  </figure>

  <figure class="panel">
    <figcaption class="font-bold">31-year ledger, 1995 → 2026 <span class="text-brand-muted font-normal text-sm">· {projs.length + undated.length} of {data.projects.length} rows · hatched = approximate span · → = ongoing</span></figcaption>
    <svg width={w - 40} height={projs.length * 13 + 30 + (undated.length ? 30 + undated.length * 13 : 0)} role="img" aria-label="Waste project ledger timeline 1995 to 2026">
      <defs>{#each ['a', 'b', 'c'] as k}<pattern id={`hatch-${k}`} width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="5" height="5" fill="#fff" /><line x1="0" y1="0" x2="0" y2="5" stroke={patColor[k]} stroke-width="2.5" /></pattern>{/each}</defs>
      {#each [1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030] as y}
        <line x1={x2(y)} x2={x2(y)} y1="14" y2={projs.length * 13 + 20} stroke="#e2e8f0" /><text x={x2(y)} y="10" font-size="10" text-anchor="middle" fill="#334155">{y}</text>
      {/each}
      {#each projs as p, i}
        {@const e = Math.max(p.end ?? p.start, p.start) + 1}
        <g role="button" tabindex="0" aria-label={`${p.id} ${p.name}, ${p.years_text}, pattern ${p.pattern}`} onclick={() => pick(p)} onkeydown={(k) => key(k, p)} style="cursor:pointer">
          <text x="0" y={22 + i * 13} font-size="9.5" font-family="var(--font-mono)" fill="#334155">{p.id}</text>
          <rect x={x2(p.start)} y={14 + i * 13} width={Math.max(4, x2(Math.min(2030, p.ongoing ? Math.max(e, 2027) : e)) - x2(p.start))} height="10" rx="2"
            fill={p.approx ? `url(#hatch-${p.pattern[0]})` : patColor[p.pattern[0]]} stroke={p.approx ? patColor[p.pattern[0]] : 'none'} stroke-dasharray={p.approx ? '3 2' : undefined} opacity={sel === p ? 1 : 0.75} />
          {#if p.approx}<text x={x2(Math.min(2030, e)) + 4} y={23 + i * 13} font-size="9" fill="#475569">≈ decades only</text>{/if}
          {#if p.ongoing || e > 2030}<text x={x2(Math.min(2030, Math.max(e, 2027))) + 3} y={23 + i * 13} font-size="9" fill="#64748b">→</text>{/if}
        </g>
      {/each}
      {#if undated.length}
        {@const y0 = projs.length * 13 + 30}
        <line x1="0" x2={w - 40} y1={y0} y2={y0} stroke="#cbd5e1" stroke-dasharray="4 3" />
        <text x="0" y={y0 + 16} font-size="10" font-family="var(--font-mono)" fill="#475569">UNDATED · sources give no usable years</text>
        {#each undated as p, i}
          <g role="button" tabindex="0" aria-label={`${p.id} ${p.name}, undated: ${p.years_text}, pattern ${p.pattern}`} onclick={() => pick(p)} onkeydown={(k) => key(k, p)} style="cursor:pointer">
            <text x="0" y={y0 + 32 + i * 13} font-size="9.5" font-family="var(--font-mono)" fill="#334155">{p.id}</text>
            <rect x={x2(1994)} y={y0 + 24 + i * 13} width="10" height="10" rx="2" fill="none" stroke={patColor[p.pattern[0]]} stroke-width="1.5" />
            <text x={x2(1994) + 16} y={y0 + 32 + i * 13} font-size="9.5" fill="#334155">{p.name.slice(0, 70)}{p.name.length > 70 ? '…' : ''} — {p.years_text}</text>
          </g>
        {/each}
      {/if}
    </svg>
  </figure>
  {/if}

  <div class="panel min-h-24" aria-live="polite">
    {#if sel}
      {#if sel.type && sel.effect}
        <p class="mono-label">{sel.date} · {sel.type} · conf {sel.confidence}</p><p class="font-bold">{sel.title}</p><p>{sel.effect}</p>
      {:else}
        <p class="mono-label">{sel.id} · {sel.type} · pattern {sel.pattern_note}</p><p class="font-bold">{sel.name}</p>
        <p class="text-sm"><strong>Years:</strong> {sel.years_text}</p><p class="text-sm"><strong>Funder / implementer:</strong> {sel.funder_implementer}</p>
        <p class="text-sm"><strong>Independent evaluation:</strong> {sel.evaluation}</p>{#if sel.flag}<p class="text-sm text-red-800">⚑ {sel.flag}</p>{/if}
      {/if}
      <p class="src mt-2">src: {sel.src}</p>
    {:else}<p class="text-brand-muted">Select a dot or bar (click, or Tab + Enter) to see the item and the file it comes from.</p>{/if}
  </div>
</div>
