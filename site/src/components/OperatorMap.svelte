<script lang="ts">
  import { onMount } from 'svelte';
  import 'maplibre-gl/dist/maplibre-gl.css';
  let { url, unmappedUrl, styleUrl = 'https://tiles.openfreemap.org/styles/positron' } = $props();
  let el: HTMLDivElement;
  let map: any;
  let gj: any = $state(null);
  let group = $state('all');
  let showDrop = $state(true);
  let sel: any = $state(null);
  let um: any = $state(null);
  const groups = [['all', 'All waste types'], ['HH.', 'Household (HH)'], ['COM.', 'Commercial'], ['IND.', 'Industrial'], ['AGR.', 'Agriculture'], ['MARINE.', 'Marine'], ['VEHICLE.', 'Vehicles / tyres'], ['MED.', 'Medical']];
  const counts = $derived.by(() => {
    if (!gj) return { e: 0, d: 0 };
    const f = gj.features.filter((x: any) => match(x));
    return { e: f.filter((x: any) => x.properties.layer === 'entity').length, d: f.filter((x: any) => x.properties.layer === 'drop_point').length };
  });
  function match(f: any) {
    const p = f.properties;
    if (p.layer === 'drop_point') return showDrop && group === 'all';
    return group === 'all' || (p.waste_types || '').split(';').some((t: string) => t.startsWith(group));
  }
  function apply() {
    if (!map || !gj || !map.getSource('ops')) return;
    map.getSource('ops').setData({ type: 'FeatureCollection', features: gj.features.filter(match) });
  }
  $effect(() => { group; showDrop; apply(); });
  onMount(() => {
    let dead = false;
    (async () => {
      const ml: any = await import('maplibre-gl');
      const workerUrl = (await import('maplibre-gl/dist/maplibre-gl-worker.mjs?worker&url')).default;
      ml.setWorkerUrl(workerUrl);
      [gj, um] = await Promise.all([fetch(url).then((r) => r.json()), unmappedUrl ? fetch(unmappedUrl).then((r) => r.json()) : null]);
      if (dead) return;
      map = new ml.Map({ container: el, style: styleUrl, fadeDuration: matchMedia('(prefers-reduced-motion: reduce)').matches ? 0 : 300, center: [80.3, 7.6], zoom: 6.6, attributionControl: { compact: false } });
      map.addControl(new ml.NavigationControl({ showCompass: false }), 'top-right');
      map.on('load', () => {
        map.addSource('ops', { type: 'geojson', data: { type: 'FeatureCollection', features: gj.features.filter(match) } });
        map.addLayer({ id: 'ops', type: 'circle', source: 'ops', paint: {
          'circle-radius': ['interpolate', ['linear'], ['zoom'], 6, 3.2, 12, 7],
          'circle-color': ['match', ['get', 'layer'], 'drop_point', '#0369a1', '#c2410c'],
          'circle-stroke-color': ['case', ['==', ['get', 'geocoded_by_atlas'], true], '#090d16', '#fff'], 'circle-stroke-width': ['case', ['==', ['get', 'geocoded_by_atlas'], true], 1.6, 1], 'circle-opacity': 0.85 } });
        map.on('click', 'ops', (e: any) => { sel = e.features[0].properties; });
        map.on('mouseenter', 'ops', () => (map.getCanvas().style.cursor = 'pointer'));
        map.on('mouseleave', 'ops', () => (map.getCanvas().style.cursor = ''));
        (window as any).__mapReady = true;
      });
    })();
    return () => { dead = true; map?.remove(); };
  });
</script>

<div class="space-y-3">
  <div class="flex flex-wrap items-center gap-3 text-sm">
    <label class="chip">Waste group
      <select bind:value={group} class="ml-1 bg-transparent">{#each groups as [v, l]}<option value={v}>{l}</option>{/each}</select>
    </label>
    <label class="chip"><input type="checkbox" bind:checked={showDrop} disabled={group !== 'all'} /> drop points</label>
    <span class="font-mono text-xs"><span style="color:#c2410c">●</span> operators {counts.e} · <span style="color:#0369a1">●</span> drop points {counts.d} · <span class="inline-block w-2.5 h-2.5 rounded-full border-2 border-[#090d16] align-middle"></span> dark ring = locality centroid (approx.)</span>
  </div>
  {#if gj?.meta?.counts}
    {@const c = gj.meta.counts}
    <p class="text-xs text-brand-secondary">Mapped: {c.entities_mapped} of {c.entities_total} operators, {c.drop_points_mapped} of {c.drop_points_total} drop points. Of these, {c.entities_geocoded_by_atlas + c.drop_points_geocoded_by_atlas} were placed for this atlas at the centre of the town named in their own address (OSM Nominatim, checked against the stated district). <strong>Not mapped ({c.entities_not_mapped + c.drop_points_not_mapped})</strong>: reasons listed below the map. No coordinates are invented.</p>
  {/if}
  <div class="grid lg:grid-cols-[1fr_300px] gap-4">
    <div bind:this={el} class="panel !p-0 h-[560px] overflow-hidden" role="region" aria-label="Map of listed waste operators and drop points in Sri Lanka. Positions are approximate."></div>
    <aside class="panel text-sm space-y-1.5" aria-live="polite">
      {#if sel}
        <p class="mono-label">{sel.layer === 'drop_point' ? 'drop point' : 'operator'} · {sel.verified_on_ground ?? 'not verified'}</p>
        <p class="font-bold">{sel.name ?? sel.point_name}</p>
        {#if sel.type}<p>{sel.type}</p>{/if}{#if sel.operator}<p>Operator: {sel.operator}</p>{/if}
        {#if sel.activity}<p><strong>Activity:</strong> {sel.activity}</p>{/if}
        <p><strong>Streams:</strong> {sel.waste_streams ?? sel.streams}</p>
        {#if sel.district}<p><strong>District:</strong> {sel.district}</p>{/if}
        {#if sel.household_access}<p><strong>Household access:</strong> {sel.household_access}</p>{/if}
        <p class="text-xs text-brand-muted">Position: {sel.coord_precision ?? 'n/a'}{sel.geocoded_by_atlas ? ' · placed by this atlas' : ''}</p>
        <p class="src">src: {sel.source_urls ?? sel.source}</p>
      {:else}<p class="text-brand-muted">Click a point. Every row is <strong>listed</strong> (CEA lists, OSM, news, operator pages). None is verified on the ground yet. Contact fields removed.</p>{/if}
    </aside>
  </div>
</div>
{#if um}
  {@const groups = Object.entries(um.rows.reduce((a: any, r: any) => { const k = r.reason.replace(/ \(tried:.*$/, '').replace(/ \(district only:.*$/, ''); (a[k] ??= []).push(r); return a; }, {})).sort((a: any, b: any) => b[1].length - a[1].length)}
  <details class="text-sm mt-3"><summary class="cursor-pointer font-semibold">Not mapped ({um.rows.length}) · why</summary>
    <ul class="mt-2 space-y-2">{#each groups as [reason, rows]}<li><strong>{reason}</strong> ({(rows as any[]).length}): <span class="text-brand-secondary">{(rows as any[]).map((r) => `${r.id} ${r.name}`).join(' · ')}</span></li>{/each}</ul>
    <p class="src mt-2">src: data/operators_unmapped.json</p>
  </details>
{/if}
