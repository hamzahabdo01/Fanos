import re

html_file = 'PharmaVista_Dashboard.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

fixes = []

# ── FIX 1: KPI Icon Chips — bg-secondary-container + text-primary → bg-primary + text-white ──
old = 'bg-fanos-secondary-container flex items-center justify-center text-fanos-primary text-xs'
new = 'bg-fanos-primary flex items-center justify-center text-white text-xs'
n = content.count(old)
content = content.replace(old, new)
fixes.append(f'Fix 1 (KPI Icon Chips): {n} replacements')

# ── FIX 2: Treemap Oncology — bg-primary-text → bg-primary, border → primary-hover ──
old = 'col-span-2 row-span-3 bg-fanos-primary-text rounded-lg p-3 flex flex-col justify-between border border-fanos-primary'
new = 'col-span-2 row-span-3 bg-fanos-primary rounded-lg p-3 flex flex-col justify-between border border-[var(--color-primary-hover)]'
n = content.count(old)
content = content.replace(old, new)
fixes.append(f'Fix 2 (Treemap Oncology): {n} replacements')

# ── FIX 3: Treemap Cardiovascular — bg-primary → bg-secondary ──
old = 'col-span-1 row-span-2 bg-fanos-primary rounded-lg p-2.5 flex flex-col justify-between'
new = 'col-span-1 row-span-2 bg-fanos-secondary rounded-lg p-2.5 flex flex-col justify-between'
n = content.count(old)
content = content.replace(old, new)
fixes.append(f'Fix 3 (Treemap Cardio): {n} replacements')

# ── FIX 4: Treemap Diabetes — bg-hover-teal → bg-tertiary ──
old = 'col-span-1 row-span-1 bg-fanos-hover-teal rounded-lg p-2 flex flex-col justify-between'
new = 'col-span-1 row-span-1 bg-fanos-tertiary rounded-lg p-2 flex flex-col justify-between'
n = content.count(old)
content = content.replace(old, new)
fixes.append(f'Fix 4 (Treemap Diabetes): {n} replacements')

# ── FIX 5: title-md CSS class — hardcoded color → CSS var ──
old = '        .title-md {\n            font-size: 20px;\n            font-weight: 600;\n            line-height: 28px;\n            color: #0a3235;\n        }'
new = '        .title-md {\n            font-size: 20px;\n            font-weight: 600;\n            line-height: 28px;\n            color: var(--color-text-primary);\n        }'
n = content.count(old)
content = content.replace(old, new)
fixes.append(f'Fix 5 (title-md CSS): {n} replacements')

# ── FIX 6: Scrollbar track — hardcoded → CSS var ──
old = '        ::-webkit-scrollbar-track {\n            background: #f0f4f6;\n        }'
new = '        ::-webkit-scrollbar-track {\n            background: var(--color-surface-low);\n        }'
n = content.count(old)
content = content.replace(old, new)
fixes.append(f'Fix 6 (Scrollbar track): {n} replacements')

# ── FIX 7: Scrollbar thumb — hardcoded → CSS vars ──
old = '        ::-webkit-scrollbar-thumb {\n            background: #bfc8c9;\n            border-radius: 4px;\n        }\n        ::-webkit-scrollbar-thumb:hover {\n            background: #707979;\n        }'
new = '        ::-webkit-scrollbar-thumb {\n            background: var(--color-gray-border);\n            border-radius: 4px;\n        }\n        ::-webkit-scrollbar-thumb:hover {\n            background: var(--color-secondary);\n        }'
n = content.count(old)
content = content.replace(old, new)
fixes.append(f'Fix 7 (Scrollbar thumb): {n} replacements')

# ── FIX 8 & 9: Sidebar inactive nav — text + hover ──
old = 'text-[var(--color-on-primary-container)] hover:bg-[var(--color-primary-dark)] hover:text-white transition-all duration-150'
new = 'text-white/70 hover:bg-white/10 hover:text-white transition-all duration-150'
n = content.count(old)
content = content.replace(old, new)
fixes.append(f'Fix 8+9 (Sidebar nav text+hover): {n} replacements')

# ── FIX 10: Filter select dropdowns ──
old = 'bg-[var(--color-primary-dark)] border border-fanos-primary text-white rounded px-2 py-1 text-[11px] focus:outline-none focus:border-[var(--color-on-primary-container)]'
new = 'bg-white/10 border border-white/20 text-white rounded px-2 py-1 text-[11px] focus:outline-none focus:border-white/50'
n = content.count(old)
content = content.replace(old, new)
fixes.append(f'Fix 10 (Filter dropdowns): {n} replacements')

# ── FIX 11: Revenue Trend "Target" chart line → on-primary-container in updateChartColors ──
old = "                window.charts['revenue-trend'].data.datasets[1].borderColor = secondary;"
new = "                window.charts['revenue-trend'].data.datasets[1].borderColor = getComputedStyle(document.documentElement).getPropertyValue('--color-on-primary-container').trim();"
n = content.count(old)
content = content.replace(old, new)
# Also fix the init value
old2 = """                        {
                            label: 'Target Target',
                            data: [400, 600, 800, 950, 1100],
                            borderColor: getComputedStyle(document.documentElement).getPropertyValue('--color-secondary').trim(),"""
new2 = """                        {
                            label: 'Target Target',
                            data: [400, 600, 800, 950, 1100],
                            borderColor: getComputedStyle(document.documentElement).getPropertyValue('--color-on-primary-container').trim(),"""
n2 = content.count(old2)
content = content.replace(old2, new2)
fixes.append(f'Fix 11 (Revenue target line): {n}+{n2} replacements')

# ── FIX 12: surface-dim Tailwind token ──
old = "                            'surface-dim': '#d6dbdd',"
new = "                            'surface-dim': 'var(--color-surface-container-high)',"
n = content.count(old)
content = content.replace(old, new)
fixes.append(f'Fix 12 (surface-dim token): {n} replacements')

# ── FIX 13: outline / outline-variant Tailwind tokens ──
old = "                            'outline': '#707979',\n                            'outline-variant': '#bfc8c9',"
new = "                            'outline': 'var(--color-gray-border)',\n                            'outline-variant': 'var(--color-surface-container-highest)',"
n = content.count(old)
content = content.replace(old, new)
fixes.append(f'Fix 13 (outline tokens): {n} replacements')

# ── FIX 14: Add --color-surface-container-highest to :root (needed for outline-variant) ──
# Already exists in :root, so just verify. Add if missing.
if '--color-surface-container-highest' not in content:
    content = content.replace(
        '--color-surface-container-high: #e5e9eb;',
        '--color-surface-container-high: #e5e9eb;\n            --color-surface-container-highest: #dfe3e5;'
    )
    fixes.append('Fix 14 (add surface-container-highest to root): 1 replacement')

# ── FIX 15: Also add --color-surface-container-high to updateTheme JS ──
old_theme = "            root.style.setProperty('--color-surface-container', surfaceContainer);"
new_theme = """            root.style.setProperty('--color-surface-container', surfaceContainer);
            root.style.setProperty('--color-surface-container-high', adjustColorBrightness(surfaceContainer, -2));
            root.style.setProperty('--color-surface-container-highest', adjustColorBrightness(surfaceContainer, -4));"""
n = content.count(old_theme)
content = content.replace(old_theme, new_theme)
fixes.append(f'Fix 15 (surface-container-high/highest dynamic): {n} replacements')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print('All audit fixes applied:')
for fix in fixes:
    print(f'  ✓ {fix}')
