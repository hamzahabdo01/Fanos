import re

html_file = 'PharmaVista_Dashboard.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure CSS variables cover everything
# Let's inject new variables into the :root block first
if '--color-primary-dark' in content and '--color-on-primary-container' not in content:
    content = content.replace('--color-primary-hover: #115e59;', '--color-primary-hover: #115e59;\n            --color-on-primary-container: #86bfc5;')

# Replacements for Tailwind classes
replacements = {
    r'bg-\[#002c30\]': 'bg-[var(--color-primary-dark)]',
    r'bg-\[#00373b\]': 'bg-[var(--color-primary-dark)]',
    r'bg-\[#0a3235\]': 'bg-fanos-primary-text',
    r'bg-\[#0b4f54\]': 'bg-fanos-primary',
    r'bg-\[#115e59\]': 'bg-fanos-hover-teal',
    r'bg-\[#86bfc5\]': 'bg-[var(--color-on-primary-container)]',
    r'bg-\[#cfd8dc\]': 'bg-fanos-gray-border',
    r'bg-\[#d5e3fc\]': 'bg-fanos-secondary-container',
    r'bg-\[#f0f4f6\]': 'bg-fanos-surface-container-low',
    r'bg-\[#f6fafc\]': 'bg-fanos-surface',
    
    r'border-\[#00201e\]': 'border-fanos-gray-border',
    r'border-\[#0b4f54\]': 'border-fanos-primary',
    r'border-\[#86bfc5\]': 'border-[var(--color-on-primary-container)]',
    
    r'text-\[#00201e\]': 'text-fanos-primary-text',
    r'text-\[#0b4f54\]': 'text-fanos-primary',
    r'text-\[#404849\]': 'text-fanos-on-surface-variant',
    r'text-\[#475569\]': 'text-fanos-secondary',
    r'text-\[#707979\]': 'text-fanos-outline',
    r'text-\[#86bfc5\]': 'text-[var(--color-on-primary-container)]',
    r'text-\[#8fd3cc\]': 'text-[var(--color-on-primary-container)]',
    r'text-\[#ba1a1a\]': 'text-fanos-error',
    r'text-\[#d97706\]': 'text-fanos-warning',
    r'text-\[#edf1f3\]': 'text-[var(--color-text-on-surface)]'
}

for old, new in replacements.items():
    content = re.sub(old, new, content)

# Also fix the setupThemeListeners to update --color-on-primary-container dynamically
# I will use string replace for this.
update_theme_func = """        function updateTheme(primary, secondary, tertiary, bg, surface) {"""
if "root.style.setProperty('--color-on-primary-container'" not in content:
    # Add logic to calculate --color-on-primary-container
    old_update = """            root.style.setProperty('--color-tertiary', tertiary);"""
    new_update = """            root.style.setProperty('--color-tertiary', tertiary);
            root.style.setProperty('--color-on-primary-container', isDarkBg ? '#97d0d6' : '#0b4f54');"""
    content = content.replace(old_update, new_update)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Colors successfully replaced!")
