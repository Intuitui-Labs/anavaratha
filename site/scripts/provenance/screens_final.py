import asyncio, json
from playwright.async_api import async_playwright
BASE='http://127.0.0.1:4322'; OUT='/workspace/viz/screens'
ARGS=['--no-sandbox','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']
async def main():
    rep={}
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=ARGS)
        # perf: JS bytes per route (no scrolling)
        for path in ['/','/lineage','/method','/data','/notes','/changelog','/atlas']:
            ctx=await b.new_context(viewport={'width':1440,'height':900}); pg=await ctx.new_page(); js=[]
            pg.on('response',lambda r: js.append(r.url.split('/')[-1]) if r.url.endswith('.js') else None)
            await pg.goto(BASE+path,wait_until='networkidle'); await pg.wait_for_timeout(800)
            rep.setdefault('js_on_load',{})[path]=js
            if path=='/atlas':
                await pg.evaluate('window.scrollTo(0, document.body.scrollHeight)'); await pg.wait_for_timeout(4000)
                rep['js_after_full_scroll_atlas']=sorted(set(js))
            await ctx.close()
        # favicon
        ctx=await b.new_context(); pg=await ctx.new_page(); r=await pg.goto(BASE+'/favicon.svg'); rep['favicon_status']=r.status; await ctx.close()
        # reduced motion + keyboard
        ctx=await b.new_context(viewport={'width':1440,'height':900},reduced_motion='reduce'); pg=await ctx.new_page(); errs=[]
        pg.on('pageerror',lambda e: errs.append(str(e))); pg.on('console',lambda m: errs.append(m.text) if m.type=='error' else None)
        await pg.goto(BASE+'/atlas',wait_until='networkidle')
        rep['reduced_motion_matches']=await pg.evaluate("matchMedia('(prefers-reduced-motion: reduce)').matches")
        rep['scroll_behavior']=await pg.evaluate("getComputedStyle(document.documentElement).scrollBehavior")
        await pg.keyboard.press('Tab'); rep['first_tab']=await pg.evaluate("document.activeElement.textContent.trim().slice(0,40)")
        await pg.locator('#timeline').scroll_into_view_if_needed(); await pg.wait_for_timeout(1500)
        await pg.locator('#timeline button').first.focus()
        for _ in range(12):
            await pg.keyboard.press('Tab')
            if await pg.evaluate("document.activeElement.getAttribute('role')==='button' && document.activeElement.tagName.toLowerCase()==='g'"): break
        rep['tab_reaches_timeline_item']=await pg.evaluate("document.activeElement.getAttribute('aria-label')")
        await pg.keyboard.press('Enter'); await pg.wait_for_timeout(200)
        rep['enter_selects']=await pg.locator('#timeline [aria-live]').inner_text()
        await pg.locator('#relations').scroll_into_view_if_needed(); await pg.wait_for_timeout(2500)
        await pg.get_by_placeholder('type 2+ letters').fill('charter'); await pg.wait_for_timeout(200)
        btn=pg.locator('#relations ul.flex button').first; await btn.focus(); await pg.keyboard.press('Enter'); await pg.wait_for_timeout(400)
        rep['find_enter_selects']=(await pg.locator('#relations aside').inner_text())[:120]
        rep['errors_reduced_motion']=errs[:5]; await ctx.close()
        # screenshots
        ctx=await b.new_context(viewport={'width':1440,'height':900}); pg=await ctx.new_page(); errs=[]
        pg.on('pageerror',lambda e: errs.append(str(e)))
        await pg.goto(BASE+'/',wait_until='networkidle'); await pg.wait_for_timeout(500)
        await pg.screenshot(path=f'{OUT}/final_1_home.png',full_page=True)
        await pg.goto(BASE+'/atlas',wait_until='networkidle'); await pg.add_style_tag(content='header.sticky{position:static !important}')
        t=pg.locator('#timeline'); await t.scroll_into_view_if_needed(); await pg.wait_for_timeout(1500)
        await pg.locator('#timeline g[role=button]').nth(4).click(); await pg.wait_for_timeout(300)
        await t.screenshot(path=f'{OUT}/final_2_timeline.png')
        r=pg.locator('#relations'); await r.scroll_into_view_if_needed(); await pg.wait_for_timeout(2500)
        await r.screenshot(path=f'{OUT}/final_lineage_zoomed_out.png')
        await pg.get_by_role('radio',name='Institutions · responsibility chain').click(); await pg.wait_for_timeout(2000)
        await r.screenshot(path=f'{OUT}/final_3_relations_institutions.png')
        m=pg.locator('#map'); await m.scroll_into_view_if_needed()
        await pg.wait_for_function('window.__mapReady === true',timeout=30000); await pg.wait_for_timeout(5000)
        await pg.get_by_text('Not mapped (66) · why').click(); await pg.wait_for_timeout(300)
        await m.screenshot(path=f'{OUT}/final_4_map.png')
        f=pg.locator('#flows'); await f.scroll_into_view_if_needed(); await pg.wait_for_timeout(1000); await f.screenshot(path=f'{OUT}/final_flows.png')
        await pg.goto(BASE+'/method',wait_until='networkidle'); await pg.screenshot(path=f'{OUT}/final_method.png',full_page=True)
        rep['errors_screens']=errs[:5]
        await b.close()
    print(json.dumps(rep,indent=1))
asyncio.run(main())
