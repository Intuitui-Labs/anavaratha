<script lang="ts">
  import { onMount } from 'svelte';
  let { data } = $props();
  const cats = [...new Set(data.cells.map((c: any) => c.category))] as string[];
  let cat = $state('concept');
  let el: HTMLDivElement;
  let Plot: any = $state(null);
  const short: Record<string, string> = {};
  data.sources.forEach((s: string) => (short[s] = s.replace(/_/g, ' ').replace('Feb20 ConceptDoc ClaudeProject', 'Feb-20 Concept Doc').replace('Feb24 docs IntuituiLabs+xlsx', 'Feb-24 docs').replace('Aug25 WasteCycles Anavaratha WC', 'Aug-25 [WC]')));
  onMount(async () => { Plot = await import('@observablehq/plot'); });
  $effect(() => {
    if (!Plot || !el) return;
    const cells = data.cells.filter((c: any) => c.category === cat);
    const rows = [...new Set(cells.map((c: any) => c.row))];
    const chart = Plot.plot({
      width: 1000, height: 40 + rows.length * 18, marginLeft: 330, marginBottom: 110, padding: 0.06,
      style: { fontFamily: 'Inter, system-ui', fontSize: '11px' },
      x: { label: null, tickRotate: -35, domain: data.sources, tickFormat: (s: string) => short[s] },
      y: { label: null, domain: rows },
      color: { type: 'sqrt', scheme: 'blues', label: 'regex hits', legend: true },
      marks: [Plot.cell(cells, { x: 'source', y: 'row', fill: (d: any) => (d.hits || null), title: (d: any) => `${d.row} × ${short[d.source]}: ${d.raw}`, inset: 0.5 }),
              Plot.text(cells, { x: 'source', y: 'row', text: (d: any) => (d.hits ? d.hits : ''), fontSize: 9, fill: (d: any) => (d.hits > 250 ? 'white' : 'black') })],
    });
    el.replaceChildren(chart);
  });
</script>
<div class="space-y-3">
  <label class="chip">Category <select bind:value={cat} class="ml-1 bg-transparent">{#each cats as c}<option>{c}</option>{/each}</select></label>
  <div bind:this={el} class="panel overflow-x-auto" role="img" aria-label={`Heatmap of ${cat} terms across 13 source layers. Hover a cell for counts.`}></div>
  <p class="src">src: {data.src} · {data.note}</p>
</div>
