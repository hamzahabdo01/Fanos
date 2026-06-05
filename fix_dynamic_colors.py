import re

html_file = 'PharmaVista_Dashboard.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# ─────────────────────────────────────────────────────────────────────────────
# 1. Add --color-tertiary to :root CSS block
# ─────────────────────────────────────────────────────────────────────────────
if '--color-tertiary' not in content:
    content = content.replace(
        '--color-secondary: #515f74;',
        '--color-secondary: #515f74;\n            --color-tertiary: #003734;'
    )
else:
    # Make sure it has a value even if it was added without one
    pass

# ─────────────────────────────────────────────────────────────────────────────
# 2. Add tertiary + on-secondary-container to Tailwind config
# ─────────────────────────────────────────────────────────────────────────────
content = content.replace(
    "'secondary': 'var(--color-secondary)',",
    "'secondary': 'var(--color-secondary)',\n                            'tertiary': 'var(--color-tertiary)',"
)
content = content.replace(
    "'on-secondary-container': '#57657a',",
    "'on-secondary-container': 'var(--color-secondary)',"
)
content = content.replace(
    "'secondary-container': '#d5e3fc',",
    "'secondary-container': 'var(--color-secondary-container)',"
)

# ─────────────────────────────────────────────────────────────────────────────
# 3. Add --color-secondary-container to :root
# ─────────────────────────────────────────────────────────────────────────────
if '--color-secondary-container' not in content:
    content = content.replace(
        '--color-tertiary: #003734;',
        '--color-tertiary: #003734;\n            --color-secondary-container: #d5e3fc;'
    )

# ─────────────────────────────────────────────────────────────────────────────
# 4. Replace hardcoded colors in chart INITIALIZATIONS with CSS var reads
#    We wrap them so the live update function also works correctly
# ─────────────────────────────────────────────────────────────────────────────

# Helper: Replace exact string occurrences in chart init sections only
# We'll target specific patterns in the renderCharts / initSparkline area

# Sparkline init - they pass color as argument
content = content.replace(
    "initSparkline('sparkline-revenue', [820, 910, 760, 1050, 980, 1100, 1230], '#0b4f54')",
    "initSparkline('sparkline-revenue', [820, 910, 760, 1050, 980, 1100, 1230], getComputedStyle(document.documentElement).getPropertyValue('--color-primary').trim())"
)
content = content.replace(
    "initSparkline('sparkline-profit', [220, 310, 180, 400, 350, 420, 490], '#0b4f54')",
    "initSparkline('sparkline-profit', [220, 310, 180, 400, 350, 420, 490], getComputedStyle(document.documentElement).getPropertyValue('--color-primary').trim())"
)
content = content.replace(
    "initSparkline('sparkline-inventory', [85, 88, 84, 91, 89, 92, 94], '#0b4f54')",
    "initSparkline('sparkline-inventory', [85, 88, 84, 91, 89, 92, 94], getComputedStyle(document.documentElement).getPropertyValue('--color-primary').trim())"
)
content = content.replace(
    "initSparkline('sparkline-yield', [88.1, 87.5, 89.0, 88.3, 89.2, 88.9, 89.7], '#0b4f54')",
    "initSparkline('sparkline-yield', [88.1, 87.5, 89.0, 88.3, 89.2, 88.9, 89.7], getComputedStyle(document.documentElement).getPropertyValue('--color-primary').trim())"
)
content = content.replace(
    "initSparkline('sparkline-compliance', [92, 93, 93.5, 93, 94, 93.8, 94.2], '#0b4f54')",
    "initSparkline('sparkline-compliance', [92, 93, 93.5, 93, 94, 93.8, 94.2], getComputedStyle(document.documentElement).getPropertyValue('--color-primary').trim())"
)

# Revenue trend chart
content = content.replace(
    """                        {
                            label: 'Actual Revenue',
                            data: [300, 500, 700, 950, 1230],
                            borderColor: '#0b4f54',""",
    """                        {
                            label: 'Actual Revenue',
                            data: [300, 500, 700, 950, 1230],
                            borderColor: getComputedStyle(document.documentElement).getPropertyValue('--color-primary').trim(),"""
)
content = content.replace(
    """                        {
                            label: 'Target Target',
                            data: [400, 600, 800, 950, 1100],
                            borderColor: '#86bfc5',""",
    """                        {
                            label: 'Target Target',
                            data: [400, 600, 800, 950, 1100],
                            borderColor: getComputedStyle(document.documentElement).getPropertyValue('--color-secondary').trim(),"""
)

# Compliance radar
content = content.replace(
    """                        data: [94, 92, 95, 90, 93, 96],
                        backgroundColor: 'rgba(11, 79, 84, 0.15)',
                        borderColor: '#0b4f54',""",
    """                        data: [94, 92, 95, 90, 93, 96],
                        backgroundColor: getComputedStyle(document.documentElement).getPropertyValue('--color-primary').trim() + '26',
                        borderColor: getComputedStyle(document.documentElement).getPropertyValue('--color-primary').trim(),"""
)

# Yield trend - planned line (secondary) and actual line (primary)
content = content.replace(
    """                        {
                            label: 'Planned',
                            data: [90, 90, 90, 90, 90],
                            borderColor: '#86bfc5',""",
    """                        {
                            label: 'Planned',
                            data: [90, 90, 90, 90, 90],
                            borderColor: getComputedStyle(document.documentElement).getPropertyValue('--color-secondary').trim(),"""
)
content = content.replace(
    """                        {
                            label: 'Actual',
                            data: [88, 89.2, 87.5, 88.3, 89.7],
                            borderColor: '#0b4f54',""",
    """                        {
                            label: 'Actual',
                            data: [88, 89.2, 87.5, 88.3, 89.7],
                            borderColor: getComputedStyle(document.documentElement).getPropertyValue('--color-primary').trim(),"""
)

# Demand forecast - historical (secondary) and forecast (tertiary)
content = content.replace(
    """                        {
                            label: 'Historical',
                            data: [220, 290, 310, null, null],
                            borderColor: '#475569',""",
    """                        {
                            label: 'Historical',
                            data: [220, 290, 310, null, null],
                            borderColor: getComputedStyle(document.documentElement).getPropertyValue('--color-secondary').trim(),"""
)
content = content.replace(
    """                        {
                            label: 'Forecast',
                            data: [null, null, 310, 340, 320],
                            borderColor: '#0b4f54',""",
    """                        {
                            label: 'Forecast',
                            data: [null, null, 310, 340, 320],
                            borderColor: getComputedStyle(document.documentElement).getPropertyValue('--color-tertiary').trim(),"""
)

# Quality scores - low range border (gray-border) and avg score bar (primary)
content = content.replace(
    """                        {
                            label: 'Low Range',
                            data: [82, 85, 80, 84, 86],
                            backgroundColor: 'transparent',
                            borderColor: '#bfc8c9',""",
    """                        {
                            label: 'Low Range',
                            data: [82, 85, 80, 84, 86],
                            backgroundColor: 'transparent',
                            borderColor: getComputedStyle(document.documentElement).getPropertyValue('--color-gray-border').trim(),"""
)
content = content.replace(
    """                        {
                            label: 'Avg Score',
                            data: [8, 7, 10, 9, 6],
                            backgroundColor: '#0b4f54',""",
    """                        {
                            label: 'Avg Score',
                            data: [8, 7, 10, 9, 6],
                            backgroundColor: getComputedStyle(document.documentElement).getPropertyValue('--color-primary').trim(),"""
)

# Top products bar
content = content.replace(
    """                    datasets: [{
                        data: [180, 142, 98, 86, 74],
                        backgroundColor: '#0b4f54',""",
    """                    datasets: [{
                        data: [180, 142, 98, 86, 74],
                        backgroundColor: getComputedStyle(document.documentElement).getPropertyValue('--color-primary').trim(),"""
)

# ─────────────────────────────────────────────────────────────────────────────
# 5. Expand updateChartColors to cover ALL secondary/tertiary datasets
# ─────────────────────────────────────────────────────────────────────────────

old_update_charts = """        function updateChartColors(primary, secondary, tertiary, axisColor) {
            // Update Sparklines
            const sparklineIds = ['sparkline-revenue', 'sparkline-profit', 'sparkline-inventory', 'sparkline-yield', 'sparkline-compliance'];
            sparklineIds.forEach(id => {
                if (window.charts[id]) {
                    window.charts[id].data.datasets[0].borderColor = primary;
                    window.charts[id].update();
                }
            });

            // Update Revenue Trend
            if (window.charts['revenue-trend']) {
                window.charts['revenue-trend'].data.datasets[0].borderColor = primary;
                window.charts['revenue-trend'].options.scales.x.ticks.color = axisColor;
                window.charts['revenue-trend'].options.scales.y.ticks.color = axisColor;
                window.charts['revenue-trend'].update();
            }"""

new_update_charts = """        function updateChartColors(primary, secondary, tertiary, axisColor) {
            // Update Sparklines
            const sparklineIds = ['sparkline-revenue', 'sparkline-profit', 'sparkline-inventory', 'sparkline-yield', 'sparkline-compliance'];
            sparklineIds.forEach(id => {
                if (window.charts[id]) {
                    window.charts[id].data.datasets[0].borderColor = primary;
                    window.charts[id].update();
                }
            });

            // Update Revenue Trend (dataset 0 = primary, dataset 1 = secondary)
            if (window.charts['revenue-trend']) {
                window.charts['revenue-trend'].data.datasets[0].borderColor = primary;
                window.charts['revenue-trend'].data.datasets[1].borderColor = secondary;
                window.charts['revenue-trend'].options.scales.x.ticks.color = axisColor;
                window.charts['revenue-trend'].options.scales.y.ticks.color = axisColor;
                window.charts['revenue-trend'].update();
            }"""

content = content.replace(old_update_charts, new_update_charts)

# Update compliance radar
content = content.replace(
    """            if (window.charts['compliance-radar']) {
                window.charts['compliance-radar'].data.datasets[0].borderColor = primary;
                window.charts['compliance-radar'].data.datasets[0].backgroundColor = primary + '26'; 
                window.charts['compliance-radar'].options.scales.r.pointLabels.color = axisColor;
                window.charts['compliance-radar'].update();
            }""",
    """            if (window.charts['compliance-radar']) {
                window.charts['compliance-radar'].data.datasets[0].borderColor = primary;
                window.charts['compliance-radar'].data.datasets[0].backgroundColor = primary + '26';
                window.charts['compliance-radar'].options.scales.r.pointLabels.color = axisColor;
                window.charts['compliance-radar'].options.scales.r.grid.color = axisColor + '44';
                window.charts['compliance-radar'].update();
            }"""
)

# Update yield trend (dataset 0 = secondary/planned, dataset 1 = primary/actual)
content = content.replace(
    """            if (window.charts['yield-trend']) {
                window.charts['yield-trend'].data.datasets[1].borderColor = primary;
                window.charts['yield-trend'].options.scales.x.ticks.color = axisColor;
                window.charts['yield-trend'].options.scales.y.ticks.color = axisColor;
                window.charts['yield-trend'].update();
            }""",
    """            if (window.charts['yield-trend']) {
                window.charts['yield-trend'].data.datasets[0].borderColor = secondary;
                window.charts['yield-trend'].data.datasets[1].borderColor = primary;
                window.charts['yield-trend'].options.scales.x.ticks.color = axisColor;
                window.charts['yield-trend'].options.scales.y.ticks.color = axisColor;
                window.charts['yield-trend'].update();
            }"""
)

# Update demand forecast (dataset 0 = secondary/historical, dataset 1 = tertiary/forecast)
content = content.replace(
    """            if (window.charts['demand-forecast']) {
                window.charts['demand-forecast'].data.datasets[1].borderColor = primary;
                window.charts['demand-forecast'].options.scales.x.ticks.color = axisColor;
                window.charts['demand-forecast'].options.scales.y.ticks.color = axisColor;
                window.charts['demand-forecast'].update();
            }""",
    """            if (window.charts['demand-forecast']) {
                window.charts['demand-forecast'].data.datasets[0].borderColor = secondary;
                window.charts['demand-forecast'].data.datasets[1].borderColor = tertiary;
                window.charts['demand-forecast'].options.scales.x.ticks.color = axisColor;
                window.charts['demand-forecast'].options.scales.y.ticks.color = axisColor;
                window.charts['demand-forecast'].update();
            }"""
)

# Update quality scores (dataset 0 = gray-border, dataset 1 = primary)
content = content.replace(
    """            if (window.charts['quality-scores']) {
                window.charts['quality-scores'].data.datasets[1].backgroundColor = primary;
                window.charts['quality-scores'].options.scales.x.ticks.color = axisColor;
                window.charts['quality-scores'].options.scales.y.ticks.color = axisColor;
                window.charts['quality-scores'].update();
            }""",
    """            if (window.charts['quality-scores']) {
                window.charts['quality-scores'].data.datasets[0].borderColor = axisColor;
                window.charts['quality-scores'].data.datasets[1].backgroundColor = primary;
                window.charts['quality-scores'].options.scales.x.ticks.color = axisColor;
                window.charts['quality-scores'].options.scales.y.ticks.color = axisColor;
                window.charts['quality-scores'].update();
            }"""
)

# ─────────────────────────────────────────────────────────────────────────────
# 6. Also update --color-secondary-container and sidebar/SVG elements in updateTheme
# ─────────────────────────────────────────────────────────────────────────────

# After where we set --color-tertiary in updateTheme, add secondary-container derivation
old_tertiary_set = "            root.style.setProperty('--color-tertiary', tertiary);\n            root.style.setProperty('--color-on-primary-container', isDarkBg ? '#97d0d6' : '#0b4f54');"
new_tertiary_set = """            root.style.setProperty('--color-tertiary', tertiary);
            root.style.setProperty('--color-on-primary-container', isDarkBg ? '#97d0d6' : '#0b4f54');
            // Derive secondary-container as a light tint of secondary
            const secR = parseInt(secondary.substring(1,3),16);
            const secG = parseInt(secondary.substring(3,5),16);
            const secB = parseInt(secondary.substring(5,7),16);
            const secContainerR = Math.min(255, Math.round(secR + (255 - secR) * 0.75));
            const secContainerG = Math.min(255, Math.round(secG + (255 - secG) * 0.75));
            const secContainerB = Math.min(255, Math.round(secB + (255 - secB) * 0.75));
            const secContainer = '#' + secContainerR.toString(16).padStart(2,'0') + secContainerG.toString(16).padStart(2,'0') + secContainerB.toString(16).padStart(2,'0');
            root.style.setProperty('--color-secondary-container', isDarkBg ? adjustColorBrightness(secondary, 30) : secContainer);
            // Derive tertiary-dark for sidebar
            const darkTertiary = adjustColorBrightness(tertiary, -20);
            root.style.setProperty('--color-tertiary-dark', darkTertiary);"""

content = content.replace(old_tertiary_set, new_tertiary_set)

# ─────────────────────────────────────────────────────────────────────────────
# 7. Fix sidebar hardcoded colors (the dark sidebar panels)
# ─────────────────────────────────────────────────────────────────────────────
# Sidebar uses bg-[var(--color-primary-dark)] and border-fanos-gray-border
# The inner sidebar background colors were converted; check remaining inline styles
content = content.replace(
    'style="background-color: rgba(0,0,0,0.15)"',
    'style="background-color: var(--color-primary-dark)"'
)

# ─────────────────────────────────────────────────────────────────────────────
# 8. Fix SVG paths/rects that still use hardcoded tertiary/secondary hex
# ─────────────────────────────────────────────────────────────────────────────
# Line ~724-725: stroke="#7ec1bb" → add JS update for tertiary
# We add an updateSvgColors call in updateTheme

old_svg_update = """            document.querySelectorAll('svg path').forEach(path => {
                if (path.getAttribute('stroke') === '#86bfc5') {
                    path.setAttribute('stroke', hoverPrimary);
                } else if (path.getAttribute('stroke') === '#7ec1bb') {
                    path.setAttribute('stroke', secondary);
                }
            });"""

new_svg_update = """            document.querySelectorAll('svg path').forEach(path => {
                const s = path.getAttribute('stroke');
                if (s && (s.startsWith('#') || s.startsWith('rgb'))) {
                    if (s === '#86bfc5' || path.dataset.colorRole === 'on-primary-container') {
                        path.setAttribute('stroke', hoverPrimary);
                        path.dataset.colorRole = 'on-primary-container';
                    } else if (s === '#7ec1bb' || path.dataset.colorRole === 'tertiary') {
                        path.setAttribute('stroke', tertiary);
                        path.dataset.colorRole = 'tertiary';
                    }
                }
            });"""

content = content.replace(old_svg_update, new_svg_update)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! All secondary and tertiary colors are now fully dynamic.")
