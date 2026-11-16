<script lang="ts">
  import { sankey, sankeyLinkHorizontal, sankeyJustify } from 'd3-sankey';
  let { data } = $props();
  const S = data.household_route_sankey;
  const R = data.hazardous_route;
  const statusColor: Record<string, string> = { yes: '#15803d', conditional: '#a16207', 'no route found': '#b91c1c', no: '#64748b', 'not found': '#94a3b8' };
  let w = $state(900);
  let hover: string | null = $state(null);
  const H = 520;
  const graph = $derived.by(() => {
    const nodes = S.nodes.map((n: string) => ({ name: n }));
    const idx = new Map(S.nodes.map((n: string, i: number) => [n, i]));
    const links = S.links.map((l: any) => ({ source: idx.get(l.source), target: idx.get(l.target), value: l.value, s: l.source, t: l.target }));
    return sankey().nodeWidth(12).nodePadding(10).nodeAlign(sankeyJustify).extent([[0, 6], [Math.max(400, w - 60), H - 6]])({ nodes, links } as any);
  });
  const typesFor = (g: string, st: string) => S.types.filter((t: any) => t.group === g && t.hh_route === st).map((t: any) => t.label).join('; ');
  const brokenIds = new Set(R.steps.filter((s: any) => s.broken).map((s: any) => s.id));
</script>

<div class="space-y-8">
  <figure class="panel" bind:clientWidth={w}>
    <figcaption class="font-bold">Waste types → household route status <span class="font-normal text-sm text-brand-muted">· unit = number of types (62), not tonnes</span></figcaption>
    <svg width={Math.max(440, w - 40)} height={H} role="img" aria-label="Sankey of waste type groups to household route status. Table follows.">
      {#each graph.links as l}
        <path d={sankeyLinkHorizontal()(l as any)} fill="none" stroke={statusColor[(l as any).t] ?? '#94a3b8'} stroke-opacity={hover && hover !== (l as any).s && hover !== (l as any).t ? 0.08 : 0.4} stroke-width={Math.max(1, (l as any).width)}>
          <title>{(l as any).s} → {(l as any).t}: {(l as any).value} types ({typesFor((l as any).s, (l as any).t)})</title>
        </path>
      {/each}
      {#each graph.nodes as n}
        {@const right = (n as any).x0 > w / 2}
        <g role="button" tabindex="0" aria-label={`${(n as any).name}, ${(n as any).value} types`} onmouseenter={() => (hover = (n as any).name)} onmouseleave={() => (hover = null)} onfocus={() => (hover = (n as any).name)} onblur={() => (hover = null)}>
          <rect x={(n as any).x0} y={(n as any).y0} width={(n as any).x1 - (n as any).x0} height={Math.max(2, (n as any).y1 - (n as any).y0)} fill={statusColor[(n as any).name] ?? '#334155'} />
          <text x={right ? (n as any).x0 - 6 : (n as any).x1 + 6} y={((n as any).y0 + (n as any).y1) / 2} dy="0.35em" text-anchor={right ? 'end' : 'start'} font-size="11.5" font-weight={right ? 700 : 500}>{(n as any).name} · {(n as any).value}</text>
        </g>
      {/each}
    </svg>
    <p class="src">src: {S.src}</p>
  </figure>

  <figure class="panel">
    <figcaption class="font-bold">Where the household hazardous route breaks <span class="font-normal text-sm text-brand-muted">· {R.frame}</span></figcaption>
    <ol class="mt-3 grid md:grid-cols-4 gap-2 text-sm">
      {#each R.steps as s, i}
        <li class={`rounded-lg border p-2.5 ${brokenIds.has(s.id) ? 'border-red-700 bg-red-50' : 'border-brand-border bg-white'}`}>
          <p class="font-mono text-xs text-brand-muted">{i + 1} · {s.status}</p><p class="font-semibold leading-snug">{s.label}</p><p class="src">{s.src.split('/').pop()}</p>
        </li>
      {/each}
    </ol>
    <ul class="mt-3 text-sm list-disc pl-5">{#each R.breaks as b}<li><strong class="text-red-800">Break:</strong> {b.why} <span class="src">({b.src.split('/').pop()})</span></li>{/each}</ul>
  </figure>

  <details class="text-sm"><summary class="cursor-pointer font-semibold">Table: all 62 waste types and their household route</summary>
    <table class="w-full mt-2 border-collapse"><thead><tr class="text-left border-b"><th>Group</th><th>Type</th><th>HH route</th><th>#ops listed</th></tr></thead>
      <tbody>{#each S.types as t}<tr class="border-b"><td>{t.group}</td><td>{t.label} <span class="src">{t.type_id}</span></td><td style="color:{statusColor[t.hh_route]}">{t.hh_route}</td><td class="font-mono">{t.ops ?? '—'}</td></tr>{/each}</tbody></table>
  </details>
</div>
