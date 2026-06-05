---
name: 'Tech-Forward Echo: Deep Eucalyptus'
colors:
  surface: '#f6fafc'
  surface-dim: '#d6dbdd'
  surface-bright: '#f6fafc'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f0f4f6'
  surface-container: '#eaeef0'
  surface-container-high: '#e5e9eb'
  surface-container-highest: '#dfe3e5'
  on-surface: '#181c1e'
  on-surface-variant: '#404849'
  inverse-surface: '#2c3133'
  inverse-on-surface: '#edf1f3'
  outline: '#707979'
  outline-variant: '#bfc8c9'
  surface-tint: '#2c676c'
  primary: '#00373b'
  on-primary: '#ffffff'
  primary-container: '#0b4f54'
  on-primary-container: '#86bfc5'
  inverse-primary: '#97d0d6'
  secondary: '#515f74'
  on-secondary: '#ffffff'
  secondary-container: '#d5e3fc'
  on-secondary-container: '#57657a'
  tertiary: '#003734'
  on-tertiary: '#ffffff'
  tertiary-container: '#00504b'
  on-tertiary-container: '#7ec1bb'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#b2edf2'
  primary-fixed-dim: '#97d0d6'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#0a4f54'
  secondary-fixed: '#d5e3fc'
  secondary-fixed-dim: '#b9c7df'
  on-secondary-fixed: '#0d1c2e'
  on-secondary-fixed-variant: '#3a485b'
  tertiary-fixed: '#abefe8'
  tertiary-fixed-dim: '#8fd3cc'
  on-tertiary-fixed: '#00201e'
  on-tertiary-fixed-variant: '#00504b'
  background: '#f6fafc'
  on-background: '#181c1e'
  surface-variant: '#dfe3e5'
typography:
  display-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 60px
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 44px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  title-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.01em
  caption:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
  max-width: 1280px
---

## Brand & Style
The design system embodies a "Tech-Forward Echo," blending high-performance enterprise utility with a calming, organic depth. The aesthetic is rooted in **Corporate Modernism** with a slight lean toward **Minimalism**, prioritizing clarity, precision, and a sophisticated professional tone.

The target audience consists of decision-makers and technical professionals who require a sense of stability and forward-thinking innovation. The UI evokes a feeling of structured reliability through the use of deep forest teals and steel slates, balanced against a crisp, airy background to ensure long-form legibility and reduced cognitive load.

## Colors
This design system utilizes a palette of Deep Eucalyptus and Steel Slate to create a commanding yet approachable interface.

- **Primary Architecture**: The core identity is driven by `#0B4F54` (Deep Corporate Teal), used for key brand moments and primary actions.
- **Secondary Core**: `#475569` (Steel Slate) provides professional neutrality for supporting UI elements and iconography.
- **Surface & Background**: A cool `#F0F4F6` background provides a fresh foundation, while cards and primary containers use pure `#FFFFFF` to "pop" off the page.
- **Interactive States**: Use `#115E59` for hover and active states of primary elements to provide a deep, satisfying tactile response.
- **Functional Semantics**: Standardized success (Emerald), warning (Amber), and critical (Rose) tones ensure immediate user comprehension of system status.

## Typography
The system exclusively employs **Plus Jakarta Sans**, a modern geometric sans-serif that offers a friendly yet professional demeanor. 

Headlines utilize tighter letter-spacing and heavier weights to command attention and establish a clear information hierarchy. Body text is optimized for readability with generous line heights. For interactive labels and captions, a medium weight (500) is preferred to maintain legibility at smaller scales. Always prioritize the Primary Text color (`#0A3235`) for high-contrast reading, switching to Secondary Slate for meta-information.

## Layout & Spacing
The design system uses a **Fixed-Fluid Hybrid Grid**. Content is housed within a maximum width of 1280px, centered on the viewport. 

- **Desktop**: A 12-column grid with 24px gutters and 64px side margins.
- **Tablet**: An 8-column grid with 20px gutters and 32px side margins.
- **Mobile**: A 4-column fluid grid with 16px gutters and 16px side margins.

The spacing rhythm follows a 4px/8px baseline, ensuring all components align to a predictable vertical and horizontal cadence. Use `xl` (40px) spacing between major sections and `md` (16px) for internal component padding.

## Elevation & Depth
This design system utilizes **Tonal Layering** combined with **Ambient Shadows** to define hierarchy.

Depth is expressed through three primary levels:
1. **Level 0 (Flat)**: The App Background (`#F0F4F6`). 
2. **Level 1 (Floating)**: Card surfaces (`#FFFFFF`). These use a soft, extra-diffused shadow: `0px 4px 20px rgba(10, 50, 53, 0.06)`.
3. **Level 2 (Active/Overlay)**: Modals and dropdowns. These use a more pronounced shadow with a slight teal tint to reinforce the brand: `0px 12px 32px rgba(10, 50, 53, 0.12)`.

Avoid heavy borders; instead, use the secondary-light color (`#CFD8DC`) as a subtle 1px stroke for elements that require structural definition against the white card surfaces.

## Shapes
The shape language is consistently **Rounded**, reflecting the soft terminals of the Plus Jakarta Sans typeface. 

- **Standard Elements**: Buttons and input fields use a 0.5rem (8px) radius.
- **Containers**: Cards and main content blocks utilize a generous 1rem (16px) radius to emphasize the "floating" tech-forward aesthetic.
- **Micro-elements**: Tooltips and small tags use a 0.25rem (4px) radius to maintain crispness at small scales.

## Components
- **Buttons**: Primary buttons are solid `#0B4F54` with white text. Hover states shift to `#115E59`. Secondary buttons use a `#CFD8DC` border with `#475569` text.
- **Cards**: Pure white backgrounds with a 16px corner radius and the Level 1 floating shadow. Internal padding is strictly 24px.
- **Input Fields**: 8px radius with a 1px `#CFD8DC` border. On focus, the border transitions to `#0B4F54` with a subtle 3px outer glow of the same color at 10% opacity.
- **Chips/Tags**: Small 4px radius. Use `#CFD8DC` (Eucalyptus Gray) for neutral categories and light tints of the functional colors (Success/Warning/Critical) for status indicators.
- **Lists**: Clean, borderless rows separated by a 1px `#F0F4F6` divider. High interactivity is signaled by a subtle background shift to `#F0F4F6` on hover.
- **Data Tables**: Header rows should use a subtle `#CFD8DC` background with uppercase 12px labels to distinguish from data rows.