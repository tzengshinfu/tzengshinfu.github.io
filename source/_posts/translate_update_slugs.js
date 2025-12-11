// translate_update_slugs.js
// Usage:
// 1. Install dependencies: npm install puppeteer
// 2. (Optional) Set BROWSER_PATH env var to full path of Chrome or Edge executable
//    e.g. setx BROWSER_PATH "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
// 3. Run: node translate_update_slugs.js

const fs = require('fs').promises;
const puppeteer = require('puppeteer');
const path = require('path');

const JSON_PATH = 'R:\\tzengshinfu.github.io\\source\\_posts\\rename_mapping.json';
const BROWSER_PATH = process.env.BROWSER_PATH || null; // set to Chrome/Edge exe if you want
const HEADLESS = false; // show browser so you can observe

function sleep(ms) { return new Promise(resolve => setTimeout(resolve, ms)); }

(async () => {
    try {
        const raw = await fs.readFile(JSON_PATH, 'utf8');
        const data = JSON.parse(raw);

        const launchOpts = { headless: HEADLESS, args: ['--start-maximized'] };
        if (BROWSER_PATH) launchOpts.executablePath = BROWSER_PATH;

        const browser = await puppeteer.launch(launchOpts);
        const page = await browser.newPage();
        await page.setViewport({ width: 1200, height: 900 });

        for (let i = 0; i < data.length; i++) {
            const obj = data[i];
            const title = obj.title || '';
            if (!title) {
                console.log(`[${i + 1}/${data.length}] skipping empty title for ${obj.old}`);
                continue;
            }

            const url = 'https://translate.google.com/?sl=auto&tl=en&text=' + encodeURIComponent(title) + '&op=translate';
            console.log(`[${i + 1}/${data.length}] Navigating to translate: ${title}`);
            await page.goto(url, { waitUntil: 'networkidle2' });

            try {
                await page.waitForSelector('span[jsname="W297wb"]', { timeout: 15000 });
                const translated = await page.$eval('span[jsname="W297wb"]', el => el.innerText.trim());
                // sanitize into slug-like string: remove punctuation, replace spaces with dashes
                let slug = translated.toLowerCase().replace(/[^a-z0-9\s-]/g, '').trim().replace(/\s+/g, '-');
                if (!slug) slug = translated.toLowerCase().trim();
                obj.slug = slug;
                console.log(`  -> translated: "${translated}" => slug: "${slug}"`);
            } catch (err) {
                console.warn(`  ! failed to extract translation for item ${i + 1}: ${err.message}`);
                // fallback: keep existing slug
            }

            // random delay 1~5 seconds
            const delay = Math.floor(Math.random() * 5000) + 1000;
            console.log(`  waiting ${delay}ms before next`);
            await sleep(delay);
        }

        // write back
        await fs.writeFile(JSON_PATH, JSON.stringify(data, null, 2), 'utf8');
        console.log('All done. File saved to', JSON_PATH);

        await browser.close();
    } catch (err) {
        console.error('Error:', err);
        process.exit(1);
    }
})();
