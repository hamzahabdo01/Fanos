import json
import os

def build_dashboard():
    # 1. Load the compiled stock data
    json_path = 'stock_data.json'
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found.")
        return
        
    with open(json_path, 'r') as f:
        stock_data = json.load(f)
        
    json_data_str = json.dumps(stock_data)
    print(f"Successfully loaded {len(stock_data)} items from JSON.")

    # 2. Define the light mode HTML content template (Fanos Clinical Framework)
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>National Stock Status & Pipeline Dashboard • Fanos Clinical</title>
    <!-- Google Fonts: Plus Jakarta Sans -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet">
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- ChartJS CDN -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <!-- SheetJS CDN (for Excel upload parsing) -->
    <script src="https://cdn.jsdelivr.net/npm/xlsx@0.18.5/dist/xlsx.full.min.js"></script>

    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['"Plus Jakarta Sans"', 'sans-serif'],
                    },
                    colors: {
                        fanos: {
                            'surface': '#fdf8f8',
                            'surface-dim': '#ddd9d8',
                            'surface-bright': '#fdf8f8',
                            'surface-lowest': '#ffffff',
                            'surface-low': '#f7f3f2',
                            'surface-container': '#f1edec',
                            'surface-high': '#ebe7e6',
                            'surface-highest': '#e5e2e1',
                            'on-surface': '#1c1b1b',
                            'on-surface-variant': '#444748',
                            'outline': '#747878',
                            'outline-variant': '#c4c7c7',
                            'primary': '#000000',
                            'on-primary': '#ffffff',
                            'secondary': '#5e5e5e',
                            'error': '#ba1a1a',
                            'success': '#10b981',
                            'warning': '#d97706'
                        }
                    }
                }
            }
        }
    </script>
    <style>
        /* Custom scrollbars */
        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        ::-webkit-scrollbar-track {
            background: #fdf8f8;
        }
        ::-webkit-scrollbar-thumb {
            background: #c4c7c7;
            border-radius: 3px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #747878;
        }

        /* Fanos Framework Typography Specs */
        h1 {
            font-family: "Plus Jakarta Sans", sans-serif;
            font-size: 36px;
            font-weight: 700;
            line-height: 44px;
            letter-spacing: -0.02em;
            color: #1c1b1b;
        }
        h2 {
            font-family: "Plus Jakarta Sans", sans-serif;
            font-size: 20px;
            font-weight: 600;
            line-height: 28px;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            color: #1c1b1b;
        }
        h3 {
            font-family: "Plus Jakarta Sans", sans-serif;
            font-size: 14px;
            font-weight: 500;
            line-height: 20px;
            color: #1c1b1b;
        }
        .body-kpi {
            font-family: "Plus Jakarta Sans", sans-serif;
            font-size: 40px;
            font-weight: 700;
            line-height: 48px;
            letter-spacing: -0.03em;
            color: #000000;
        }
        .body-medium {
            font-family: "Plus Jakarta Sans", sans-serif;
            font-size: 14px;
            font-weight: 400;
            line-height: 22px;
            color: #444748;
        }
        .body-small {
            font-family: "Plus Jakarta Sans", sans-serif;
            font-size: 11px;
            font-weight: 400;
            line-height: 16px;
            color: #747878;
        }

        /* Structure and Borders */
        .fanos-card {
            background-color: #ffffff;
            border: 1px solid #ebe7e6;
            border-radius: 8px; /* Consistent 8px radius */
            box-shadow: none; /* Flatness - no ambient shadows */
            transition: border-color 0.15s ease;
        }
        .fanos-card:hover {
            border-color: #747878;
        }
        .fanos-sidebar {
            width: 240px;
            border-right: 1px solid #c4c7c7;
            background-color: #ffffff;
            height: 100vh;
            position: fixed;
            top: 0;
            left: 0;
            z-index: 50;
        }
        .fanos-main {
            margin-left: 240px;
            padding: 40px;
            background-color: #fdf8f8;
            min-height: 100vh;
        }

        /* Active Nav Item Indicator */
        .fanos-nav-item.active {
            border-left: 2px solid #000000;
            background-color: #f1edec;
            color: #000000;
            font-weight: 600;
        }
        .fanos-nav-item {
            border-left: 2px solid transparent;
            transition: all 0.15s ease;
        }
        .fanos-nav-item:hover {
            background-color: #f7f3f2;
            color: #000000;
        }

        /* Active selections & states */
        .fanos-input {
            background-color: #ffffff;
            border: 1px solid #c4c7c7;
            border-radius: 8px;
            transition: all 0.15s ease;
        }
        .fanos-input:focus {
            border: 2px solid #000000;
            outline: none;
        }

        .fanos-btn-primary {
            background-color: #000000;
            color: #ffffff;
            border: 1px solid #000000;
            border-radius: 8px;
            font-weight: 600;
            transition: all 0.15s ease;
        }
        .fanos-btn-primary:hover {
            background-color: #313030;
            border-color: #313030;
        }
        .fanos-btn-primary:active {
            background-color: #1c1b1b;
            border: 2px solid #000000;
        }

        .fanos-btn-secondary {
            background-color: #ffffff;
            color: #000000;
            border: 1px solid #000000;
            border-radius: 8px;
            font-weight: 600;
            transition: all 0.15s ease;
        }
        .fanos-btn-secondary:hover {
            background-color: #f1edec;
        }

        .fanos-btn-tertiary {
            color: #000000;
            font-weight: 600;
            transition: all 0.15s ease;
        }
        .fanos-btn-tertiary:hover {
            background-color: #f7f3f2;
            border-radius: 8px;
        }

        /* Alerts and signals (used exclusively for status) */
        .signal-success { color: #10b981; }
        .signal-warning { color: #d97706; }
        .signal-error { color: #ba1a1a; }
        .signal-neutral { color: #000000; }

        .badge-success { background-color: #d1fae5; color: #065f46; border: 1px solid #a7f3d0; }
        .badge-warning { background-color: #fef3c7; color: #92400e; border: 1px solid #fde68a; }
        .badge-error { background-color: #fee2e2; color: #ba1a1a; border: 1px solid #fecaca; }
        .badge-neutral { background-color: #f1edec; color: #444748; border: 1px solid #c4c7c7; }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-5px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .animate-fade-in {
            animation: fadeIn 0.3s ease-out forwards;
        }
    </style>
</head>
<body class="bg-fanos-surface text-fanos-on-surface font-sans overflow-x-hidden">

    <!-- Persistent Sidebar -->
    <aside class="fanos-sidebar flex flex-col justify-between p-6">
        <div class="space-y-8">
            <!-- Brand Logo -->
            <div class="flex items-center gap-3 pb-2 border-b border-fanos-surface-highest">
                <div class="w-8 h-8 rounded bg-black flex items-center justify-center text-white font-black text-sm">
                    F
                </div>
                <div>
                    <h2 class="text-sm font-bold tracking-widest text-black mb-0">FANOS</h2>
                    <p class="text-[9px] font-bold text-fanos-outline uppercase tracking-wider">Clinical Framework</p>
                </div>
            </div>

            <!-- Navigation Menu -->
            <nav class="space-y-1">
                <a href="#kpi-section" class="fanos-nav-item active flex items-center gap-3 px-4 py-2.5 text-xs font-medium text-fanos-on-surface-variant">
                    <i class="fa-solid fa-chart-line text-sm w-4"></i>
                    <span>Dashboard KPIs</span>
                </a>
                <a href="#charts-section" class="fanos-nav-item flex items-center gap-3 px-4 py-2.5 text-xs font-medium text-fanos-on-surface-variant">
                    <i class="fa-solid fa-chart-pie text-sm w-4"></i>
                    <span>Data Visualizations</span>
                </a>
                <a href="#hubs-section" class="fanos-nav-item flex items-center gap-3 px-4 py-2.5 text-xs font-medium text-fanos-on-surface-variant">
                    <i class="fa-solid fa-warehouse text-sm w-4"></i>
                    <span>Regional Hubs</span>
                </a>
                <a href="#audits-section" class="fanos-nav-item flex items-center gap-3 px-4 py-2.5 text-xs font-medium text-fanos-on-surface-variant">
                    <i class="fa-solid fa-heart-pulse text-sm w-4"></i>
                    <span>Critical Audits</span>
                </a>
                <a href="#explorer-section" class="fanos-nav-item flex items-center gap-3 px-4 py-2.5 text-xs font-medium text-fanos-on-surface-variant">
                    <i class="fa-solid fa-list text-sm w-4"></i>
                    <span>Inventory Explorer</span>
                </a>
            </nav>
        </div>

        <!-- Sidebar Ingest Section -->
        <div class="space-y-4 pt-6 border-t border-fanos-surface-highest">
            <div class="p-4 bg-fanos-surface-low rounded-[8px] border border-fanos-surface-high">
                <span class="text-[10px] text-fanos-outline font-bold uppercase tracking-wider block mb-1">Ingestion Engine</span>
                <p class="body-small mb-3">Load standard EPSS Excel report for on-the-fly re-calculation.</p>
                
                <label for="excel-upload" class="cursor-pointer fanos-btn-secondary px-3 py-1.5 text-xs flex items-center justify-center gap-1.5 w-full text-center">
                    <i class="fa-solid fa-file-excel"></i>
                    <span>Upload Report</span>
                    <input type="file" id="excel-upload" accept=".xlsx,.xls" class="hidden">
                </label>
            </div>
            
            <div class="text-[9px] text-fanos-outline text-center">
                EPSS Logistics System • v3.2
            </div>
        </div>
    </aside>

    <!-- Main Canvas -->
    <main class="fanos-main space-y-10">

        <!-- Main Header -->
        <header class="flex flex-col md:flex-row items-start md:items-center justify-between gap-4 pb-6 border-b border-fanos-surface-highest">
            <div>
                <p class="body-small font-bold uppercase tracking-wider text-fanos-outline">National Stock Control System</p>
                <h1 class="mt-1">National Stock Status & Pipeline</h1>
                <p class="body-medium mt-1">Ethiopian Pharmaceutical Supply Service (EPSS) • Miscellaneous Stock Report Summary</p>
            </div>

            <!-- Inline Global Search -->
            <div class="relative w-full md:w-80 shrink-0">
                <i class="fa-solid fa-search absolute left-3.5 top-1/2 -translate-y-1/2 text-fanos-outline text-xs"></i>
                <input type="text" id="global-search" placeholder="Search items description, units..." class="w-full pl-9 pr-4 py-2 fanos-input text-xs placeholder-fanos-outline text-fanos-on-surface">
            </div>
        </header>

        <!-- Alert Notification for Updates -->
        <div id="upload-success-alert" class="hidden p-4 rounded-[8px] badge-success flex items-center justify-between gap-3 animate-fade-in">
            <div class="flex items-center gap-3">
                <i class="fa-solid fa-circle-check text-base"></i>
                <div>
                    <h3 class="font-bold text-xs">DATA COMPILATION COMPLETED</h3>
                    <p class="body-small text-emerald-800">Successfully loaded standard EPSS report. Re-rendered all KPIs, charts, map allocations, and audit lists.</p>
                </div>
            </div>
            <button onclick="document.getElementById('upload-success-alert').classList.add('hidden')" class="text-emerald-800 hover:text-black"><i class="fa-solid fa-xmark"></i></button>
        </div>

        <!-- KPI Summary Grid -->
        <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-6" id="kpi-section">
            <!-- SOH Card -->
            <div class="fanos-card p-6 flex flex-col justify-between min-h-[120px]">
                <span class="body-small font-bold uppercase tracking-wider">Total National SOH</span>
                <div class="body-kpi mt-2" id="kpi-soh">-</div>
                <span class="body-small mt-2" id="kpi-soh-sub">- items loaded</span>
            </div>

            <!-- AMC Card -->
            <div class="fanos-card p-6 flex flex-col justify-between min-h-[120px]">
                <span class="body-small font-bold uppercase tracking-wider">National AMC</span>
                <div class="body-kpi mt-2" id="kpi-amc">-</div>
                <span class="body-small mt-2 text-fanos-outline">Monthly Average Burn</span>
            </div>

            <!-- Stockout Rate Card -->
            <div class="fanos-card p-6 flex flex-col justify-between min-h-[120px]">
                <span class="body-small font-bold uppercase tracking-wider text-fanos-error">Stockout Rate</span>
                <div class="body-kpi mt-2 signal-error" id="kpi-stockout">-%</div>
                <span class="body-small mt-2 text-fanos-error font-medium" id="kpi-stockout-count">- items empty</span>
            </div>

            <!-- Overstock Rate Card -->
            <div class="fanos-card p-6 flex flex-col justify-between min-h-[120px]">
                <span class="body-small font-bold uppercase tracking-wider text-fanos-warning">Overstocked Rate</span>
                <div class="body-kpi mt-2 signal-warning" id="kpi-overstock">-%</div>
                <span class="body-small mt-2 text-fanos-warning font-medium" id="kpi-overstock-count">- items surplus</span>
            </div>

            <!-- Pipeline Active Orders -->
            <div class="fanos-card p-6 flex flex-col justify-between min-h-[120px]">
                <span class="body-small font-bold uppercase tracking-wider">Pipeline Funnel</span>
                <div class="body-kpi mt-2" id="kpi-pipeline">-</div>
                <span class="body-small mt-2 text-fanos-outline" id="kpi-pipeline-val">- units pending</span>
            </div>
        </section>

        <!-- Dynamic Filter Ribbon -->
        <section class="fanos-card p-5 flex flex-wrap items-center justify-between gap-4">
            <div class="flex flex-wrap items-center gap-3 w-full lg:w-auto">
                <span class="body-small font-bold text-fanos-outline uppercase tracking-wider flex items-center gap-1.5"><i class="fa-solid fa-filter"></i> Filters:</span>
                
                <!-- Stock Status Filter -->
                <select id="filter-status" class="px-3 py-1.5 fanos-input text-xs text-fanos-on-surface focus:outline-none">
                    <option value="">All Stock Levels</option>
                    <option value="stockout">Critical Stockout (MOS = 0)</option>
                    <option value="understocked">Understocked (0 < MOS < 3)</option>
                    <option value="adequate">Adequate (3 <= MOS <= 6)</option>
                    <option value="overstocked">Overstocked (MOS > 6)</option>
                </select>

                <!-- VEN Filter -->
                <select id="filter-ven" class="px-3 py-1.5 fanos-input text-xs text-fanos-on-surface focus:outline-none">
                    <option value="">All VEN Categories</option>
                    <option value="V">Vital (V)</option>
                    <option value="E">Essential (E)</option>
                    <option value="N">Non-Essential (N)</option>
                    <option value="L">Local / Lab (L)</option>
                </select>

                <!-- Hub Filter -->
                <select id="filter-hub" class="px-3 py-1.5 fanos-input text-xs text-fanos-on-surface focus:outline-none">
                    <option value="">All Hub Locations</option>
                </select>
            </div>
            
            <div class="flex items-center gap-4 text-xs">
                <span class="body-small font-bold">ACTIVE FILTER COUNT: <strong id="filter-active-count" class="text-black bg-fanos-surface-highest px-1.5 py-0.5 rounded">0</strong></span>
                <span class="text-fanos-surface-highest">|</span>
                <button id="btn-reset-filters" class="fanos-btn-tertiary px-2 py-1 text-xs"><i class="fa-solid fa-rotate-left mr-1"></i> Reset Filters</button>
            </div>
        </section>

        <!-- Visualizations Block (Pure Clinical Contrast Charts) -->
        <section class="grid grid-cols-1 lg:grid-cols-3 gap-6" id="charts-section">
            <!-- Chart 1: Stock Status Distribution -->
            <div class="fanos-card p-6 flex flex-col justify-between h-[340px]">
                <div>
                    <h2 class="text-xs tracking-wider mb-1">Stock Status Distribution</h2>
                    <p class="body-small">Proportional inventory segments by months of stock (MOS)</p>
                </div>
                <div class="w-full h-48 flex items-center justify-center">
                    <canvas id="chart-stock-status"></canvas>
                </div>
            </div>

            <!-- Chart 2: VEN Classification -->
            <div class="fanos-card p-6 flex flex-col justify-between h-[340px]">
                <div>
                    <h2 class="text-xs tracking-wider mb-1">VEN Class Counts</h2>
                    <p class="body-small">Absolute product counts by clinical importance rating</p>
                </div>
                <div class="w-full h-48">
                    <canvas id="chart-ven"></canvas>
                </div>
            </div>

            <!-- Chart 3: Pipeline Status Funnel -->
            <div class="fanos-card p-6 flex flex-col justify-between h-[340px]">
                <div>
                    <h2 class="text-xs tracking-wider mb-1">Pipeline Volume Summary</h2>
                    <p class="body-small">Absolute logistics quantities currently in progress</p>
                </div>
                <div class="w-full h-48">
                    <canvas id="chart-pipeline"></canvas>
                </div>
            </div>
        </section>

        <!-- Regional Hubs Comparative explorer -->
        <section class="grid grid-cols-1 lg:grid-cols-3 gap-6" id="hubs-section">
            <!-- Hub Table -->
            <div class="lg:col-span-2 fanos-card p-6 flex flex-col justify-between min-h-[440px]">
                <div class="flex items-center justify-between border-b border-fanos-surface-high pb-4 mb-4">
                    <div>
                        <h2 class="text-xs tracking-wider">Regional Hub Status Comparative</h2>
                        <p class="body-small">Calculations representing local SOH and stockout rates at all 19 EPSS hubs</p>
                    </div>
                    <span class="px-2.5 py-1 bg-fanos-surface-low border border-fanos-surface-highest text-xs font-semibold rounded-[8px]" id="total-hubs-badge">19 Hubs</span>
                </div>

                <!-- Hubs Data Grid -->
                <div class="overflow-y-auto max-h-[340px] w-full">
                    <table class="w-full text-xs text-left border-collapse">
                        <thead>
                            <tr class="border-b border-fanos-surface-highest text-fanos-outline font-bold uppercase tracking-wider pb-2">
                                <th class="py-2.5 px-3">Hub Name</th>
                                <th class="py-2.5 px-3 text-right">Local SOH</th>
                                <th class="py-2.5 px-3 text-right">Stockout Rate</th>
                                <th class="py-2.5 px-3 text-center">National Capacity Share</th>
                                <th class="py-2.5 px-3 text-center">Action</th>
                            </tr>
                        </thead>
                        <tbody id="hub-summary-tbody" class="divide-y divide-fanos-surface-high text-fanos-on-surface">
                            <!-- Populated by JS -->
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Hub Detail Panel (Paper-on-Desk Concept) -->
            <div class="fanos-card p-6 border-2 border-black bg-white flex flex-col justify-between min-h-[440px]">
                <div class="space-y-4">
                    <div class="border-b border-fanos-surface-high pb-3">
                        <span class="body-small font-bold uppercase tracking-wider text-fanos-outline block">Selected Hub Node</span>
                        <h2 class="text-lg mt-1" id="hub-detail-name">National Center</h2>
                    </div>

                    <!-- Hub statistics -->
                    <div class="grid grid-cols-2 gap-3 py-1">
                        <div class="bg-fanos-surface-low border border-fanos-surface-high p-3 rounded-[8px]">
                            <span class="body-small font-bold uppercase text-fanos-outline block">Local SOH</span>
                            <span class="text-base font-bold text-black mt-1 block" id="hub-detail-soh">-</span>
                        </div>
                        <div class="bg-fanos-surface-low border border-fanos-surface-high p-3 rounded-[8px]">
                            <span class="body-small font-bold uppercase text-fanos-outline block">Stockout Rate</span>
                            <span class="text-base font-bold signal-error mt-1 block" id="hub-detail-stockout">-%</span>
                        </div>
                    </div>

                    <!-- Hub critical stockouts -->
                    <div class="space-y-2">
                        <h3 class="font-bold text-xs uppercase tracking-wider text-black flex items-center gap-1.5"><i class="fa-solid fa-triangle-exclamation text-fanos-error"></i> Critical Stockouts Here</h3>
                        <p class="body-small" id="hub-detail-stockout-count-desc">Select a hub to generate missing Vital drugs.</p>
                        
                        <div class="overflow-y-auto max-h-[170px] space-y-2 pr-2" id="hub-detail-stockouts-list">
                            <!-- Populated by JS -->
                        </div>
                    </div>
                </div>

                <div class="text-center border-t border-fanos-surface-high pt-3 text-xs text-fanos-outline">
                    Click any hub in the left table for audit.
                </div>
            </div>
        </section>

        <!-- Vital Drug Exceptional Audits -->
        <section class="grid grid-cols-1 lg:grid-cols-2 gap-6" id="audits-section">
            <!-- Left: Critical Vital Stockouts -->
            <div class="fanos-card p-6 border-t-4 border-t-fanos-error flex flex-col justify-between min-h-[380px]">
                <div class="flex items-center justify-between border-b border-fanos-surface-high pb-4 mb-4">
                    <div>
                        <h2 class="text-xs tracking-wider text-fanos-error flex items-center gap-1.5"><i class="fa-solid fa-triangle-exclamation"></i> Critical Vital Stockouts</h2>
                        <p class="body-small">Vital items (VEN = V) with zero Months of Stock (Adj MOS = 0), sorted by AMC desc</p>
                    </div>
                    <span class="px-2 py-0.5 rounded-[8px] badge-error text-xs font-bold" id="critical-stockouts-total">- Items</span>
                </div>

                <div class="overflow-y-auto max-h-[280px] w-full">
                    <table class="w-full text-xs text-left border-collapse">
                        <thead>
                            <tr class="border-b border-fanos-surface-highest text-fanos-outline font-bold uppercase tracking-wider pb-2">
                                <th class="py-2 px-2">Item Description</th>
                                <th class="py-2 px-2 text-center">Unit</th>
                                <th class="py-2 px-2 text-right">Consump. (AMC)</th>
                                <th class="py-2 px-2 text-center">Pipeline</th>
                            </tr>
                        </thead>
                        <tbody id="critical-vitals-tbody" class="divide-y divide-fanos-surface-high text-fanos-on-surface">
                            <!-- Populated by JS -->
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Right: Overstocked Vital Assets -->
            <div class="fanos-card p-6 border-t-4 border-t-fanos-warning flex flex-col justify-between min-h-[380px]">
                <div class="flex items-center justify-between border-b border-fanos-surface-high pb-4 mb-4">
                    <div>
                        <h2 class="text-xs tracking-wider text-fanos-warning flex items-center gap-1.5"><i class="fa-solid fa-box-open"></i> Overstocked Vital Assets</h2>
                        <p class="body-small">Vital items (VEN = V) with surplus supply (Adj MOS > 12), sorted by surplus</p>
                    </div>
                    <span class="px-2 py-0.5 rounded-[8px] badge-warning text-xs font-bold" id="overstocked-vitals-total">- Items</span>
                </div>

                <div class="overflow-y-auto max-h-[280px] w-full">
                    <table class="w-full text-xs text-left border-collapse">
                        <thead>
                            <tr class="border-b border-fanos-surface-highest text-fanos-outline font-bold uppercase tracking-wider pb-2">
                                <th class="py-2 px-2">Item Description</th>
                                <th class="py-2 px-2 text-center">Unit</th>
                                <th class="py-2 px-2 text-right">Total SOH</th>
                                <th class="py-2 px-2 text-center">Months (AdjMOS)</th>
                            </tr>
                        </thead>
                        <tbody id="overstocked-vitals-tbody" class="divide-y divide-fanos-surface-high text-fanos-on-surface">
                            <!-- Populated by JS -->
                        </tbody>
                    </table>
                </div>
            </div>
        </section>

        <!-- Detailed Product Explorer (Grid) -->
        <section class="fanos-card p-6 space-y-4" id="explorer-section">
            <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 border-b border-fanos-surface-high pb-4">
                <div>
                    <h2 class="text-xs tracking-wider">Complete Inventory Explorer</h2>
                    <p class="body-small">Audit and filter all 549 pharmaceutical stock status records in real-time</p>
                </div>
                <div class="text-xs text-fanos-outline">
                    Showing <strong id="table-row-count-showing" class="text-black bg-fanos-surface-highest px-1.5 py-0.5 rounded">0</strong> of <strong id="table-row-count-total" class="text-slate-600">0</strong> items
                </div>
            </div>

            <!-- Table Responsive Wrap -->
            <div class="overflow-x-auto w-full">
                <table class="w-full text-xs text-left border-collapse whitespace-nowrap">
                    <thead>
                        <tr class="border-b border-fanos-outline text-fanos-outline font-bold uppercase tracking-wider">
                            <th class="py-3 px-3 text-center">SN</th>
                            <th class="py-3 px-3">Item Description</th>
                            <th class="py-3 px-3 text-center">Unit</th>
                            <th class="py-3 px-3 text-center">VEN</th>
                            <th class="py-3 px-3 text-right">National SOH</th>
                            <th class="py-3 px-3 text-right">AMC</th>
                            <th class="py-3 px-3 text-center">MOS</th>
                            <th class="py-3 px-3 text-center">Adj MOS</th>
                            <th class="py-3 px-3 text-center">Pipeline Deliveries</th>
                            <th class="py-3 px-3">Expiry Profile</th>
                        </tr>
                    </thead>
                    <tbody id="explorer-tbody" class="divide-y divide-fanos-surface-high text-fanos-on-surface">
                        <!-- Populated by JS -->
                    </tbody>
                </table>
            </div>

            <!-- Pagination Control -->
            <div class="flex items-center justify-between gap-4 pt-4 border-t border-fanos-surface-high text-xs">
                <div>
                    <span>Show: </span>
                    <select id="explorer-page-size" class="px-2 py-1 fanos-input text-xs text-fanos-on-surface focus:outline-none">
                        <option value="15">15 rows</option>
                        <option value="30">30 rows</option>
                        <option value="50">50 rows</option>
                        <option value="100">100 rows</option>
                    </select>
                </div>
                
                <div class="flex items-center gap-3">
                    <button id="btn-prev-page" class="fanos-btn-secondary px-3 py-1.5 text-xs disabled:opacity-40" disabled><i class="fa-solid fa-angle-left mr-1"></i> Prev</button>
                    <span class="body-small">Page <strong id="explorer-current-page" class="text-black">1</strong> of <strong id="explorer-total-pages" class="text-fanos-outline">1</strong></span>
                    <button id="btn-next-page" class="fanos-btn-secondary px-3 py-1.5 text-xs disabled:opacity-40">Next <i class="fa-solid fa-angle-right ml-1"></i></button>
                </div>
            </div>
        </section>

    </main>

    <!-- Footer -->
    <footer class="fanos-card bg-white mt-12 py-8 px-6 text-center text-xs text-fanos-outline border-t border-fanos-surface-high ml-[240px]">
        <p class="font-bold">Fanos Clinical Logistics Framework • AUTHORITATIVE MEDICAL AUDITING</p>
        <p class="mt-1">© 2026 Ethiopian Pharmaceutical Supply Service (EPSS). All Rights Reserved.</p>
    </footer>

    <!-- JSON DATA EMBED -->
    <script>
        window.INITIAL_DATA = __INITIAL_DATA_PLACEHOLDER__;
    </script>

    <!-- Core App Logic -->
    <script>
        // Setup initial variables
        let currentData = [...window.INITIAL_DATA];
        const hubNames = [
            'Adama', 'Addis Ababa', 'Addis Ababa 2', 'Arba Minch', 'Assosa', 'Bahir Dar', 
            'Dessie', 'Dire Dawa', 'Gambella', 'Gondar', 'Hawassa', 'Jigjiga', 'Jimma', 
            'Kebri Dehar', 'Mekele', 'Negele Borena', 'Nekemte', 'Semera', 'Shire'
        ];

        // Pagination and State
        let explorerPage = 1;
        let explorerPageSize = 15;
        let selectedHubName = 'National Center';
        
        // Chart references to allow updates
        let chartStockStatus = null;
        let chartVen = null;
        let chartPipeline = null;

        // On Load Initializer
        window.addEventListener('DOMContentLoaded', () => {
            initHubDropdown();
            initResetButton();
            renderDashboard(currentData);
            
            // Search listener
            document.getElementById('global-search').addEventListener('input', () => {
                explorerPage = 1;
                filterAndRender();
            });

            // Filter dropdown listeners
            document.getElementById('filter-status').addEventListener('change', () => { explorerPage = 1; filterAndRender(); });
            document.getElementById('filter-ven').addEventListener('change', () => { explorerPage = 1; filterAndRender(); });
            document.getElementById('filter-hub').addEventListener('change', () => { explorerPage = 1; filterAndRender(); });

            // Pagination listeners
            document.getElementById('explorer-page-size').addEventListener('change', (e) => {
                explorerPageSize = parseInt(e.target.value);
                explorerPage = 1;
                filterAndRender();
            });

            document.getElementById('btn-prev-page').addEventListener('click', () => {
                if (explorerPage > 1) {
                    explorerPage--;
                    filterAndRender();
                }
            });

            document.getElementById('btn-next-page').addEventListener('click', () => {
                const totalPages = Math.ceil(getFilteredData().length / explorerPageSize);
                if (explorerPage < totalPages) {
                    explorerPage++;
                    filterAndRender();
                }
            });

            // Excel Upload Listener
            document.getElementById('excel-upload').addEventListener('change', handleExcelUpload);
        });

        // Initialize Hub drop downs
        function initHubDropdown() {
            const selectHub = document.getElementById('filter-hub');
            // Clear except first
            selectHub.innerHTML = '<option value="">All Hub Locations</option>';
            hubNames.forEach(h => {
                const option = document.createElement('option');
                option.value = h;
                option.textContent = h;
                selectHub.appendChild(option);
            });
        }

        // Initialize Reset button
        function initResetButton() {
            document.getElementById('btn-reset-filters').addEventListener('click', () => {
                document.getElementById('global-search').value = '';
                document.getElementById('filter-status').value = '';
                document.getElementById('filter-ven').value = '';
                document.getElementById('filter-hub').value = '';
                explorerPage = 1;
                filterAndRender();
            });
        }

        // Get filter counts and raw data matching search/filters
        function getFilteredData() {
            const searchQuery = document.getElementById('global-search').value.toLowerCase().trim();
            const statusFilter = document.getElementById('filter-status').value;
            const venFilter = document.getElementById('filter-ven').value;
            const hubFilter = document.getElementById('filter-hub').value;

            return currentData.filter(item => {
                // Search match
                const matchSearch = !searchQuery || 
                    item.item.toLowerCase().includes(searchQuery) ||
                    (item.unit && item.unit.toLowerCase().includes(searchQuery));

                // VEN match
                const matchVen = !venFilter || item.ven === venFilter;

                // Hub match
                const matchHub = !hubFilter || item.hubs[hubFilter] > 0;

                // Status match based on National MOS
                let matchStatus = true;
                if (statusFilter) {
                    const mos = item.mos;
                    if (statusFilter === 'stockout') {
                        matchStatus = (mos === 0);
                    } else if (statusFilter === 'understocked') {
                        matchStatus = (mos > 0 && mos < 3);
                    } else if (statusFilter === 'adequate') {
                        matchStatus = (mos >= 3 && mos <= 6);
                    } else if (statusFilter === 'overstocked') {
                        matchStatus = (mos > 6);
                    }
                }

                return matchSearch && matchVen && matchHub && matchStatus;
            });
        }

        // Helper to trigger UI refresh based on filters
        function filterAndRender() {
            const filtered = getFilteredData();
            
            // Update filter badges count
            let filterCount = 0;
            if (document.getElementById('global-search').value) filterCount++;
            if (document.getElementById('filter-status').value) filterCount++;
            if (document.getElementById('filter-ven').value) filterCount++;
            if (document.getElementById('filter-hub').value) filterCount++;
            document.getElementById('filter-active-count').textContent = filterCount;

            renderExplorerTable(filtered);
        }

        // Main function to render and rebuild the entire dashboard
        function renderDashboard(data) {
            // 1. Calculations & KPIs
            let totalSOH = 0;
            let totalAMC = 0;
            let stockoutCount = 0;
            let overstockCount = 0;
            let pipelineCount = 0;
            let pipelineVolume = 0;

            let venCounts = { 'V': 0, 'E': 0, 'N': 0, 'L': 0, 'UNKNOWN': 0 };
            let stockStatusCounts = { 'stockout': 0, 'understocked': 0, 'adequate': 0, 'overstocked': 0 };

            data.forEach(item => {
                totalSOH += item.soh;
                totalAMC += item.amc;
                
                // Categorize MOS
                if (item.mos === 0) {
                    stockoutCount++;
                    stockStatusCounts['stockout']++;
                } else if (item.mos < 3) {
                    stockStatusCounts['understocked']++;
                } else if (item.mos <= 6) {
                    stockStatusCounts['adequate']++;
                } else {
                    overstockCount++;
                    stockStatusCounts['overstocked']++;
                }

                // VEN Categorize
                const v = item.ven;
                if (venCounts.hasOwnProperty(v)) {
                    venCounts[v]++;
                } else {
                    venCounts['UNKNOWN']++;
                }

                // Pipeline
                if (item.ordered_qty > 0 || item.shipped_qty > 0) {
                    pipelineCount++;
                    pipelineVolume += (item.ordered_qty + item.shipped_qty);
                }
            });

            const totalItems = data.length || 1;
            const stockoutRate = (stockoutCount / totalItems) * 100;
            const overstockRate = (overstockCount / totalItems) * 100;

            // Update UI KPIs
            document.getElementById('kpi-soh').textContent = totalSOH.toLocaleString(undefined, { maximumFractionDigits: 0 });
            document.getElementById('kpi-soh-sub').textContent = `${data.length} Items Loaded`;
            document.getElementById('kpi-amc').textContent = totalAMC.toLocaleString(undefined, { maximumFractionDigits: 0 });
            
            // Set dynamic KPI text classes (pure clinical color semantics)
            const stockoutKpi = document.getElementById('kpi-stockout');
            stockoutKpi.textContent = `${stockoutRate.toFixed(1)}%`;
            document.getElementById('kpi-stockout-count').textContent = `${stockoutCount} Vital Drug Outages`;
            
            const overstockKpi = document.getElementById('kpi-overstock');
            overstockKpi.textContent = `${overstockRate.toFixed(1)}%`;
            document.getElementById('kpi-overstock-count').textContent = `${overstockCount} Products in Surplus`;

            document.getElementById('kpi-pipeline').textContent = `${pipelineCount} Items`;
            document.getElementById('kpi-pipeline-val').textContent = `${pipelineVolume.toLocaleString(undefined, { maximumFractionDigits: 0 })} Units Ordered`;

            // 2. Charts
            renderCharts(stockStatusCounts, venCounts, data);

            // 3. Populate Hub Tables & Selected Hub Detail Panel
            renderHubSummaryTable(data);
            updateHubDetailPanel(selectedHubName, data);

            // 4. Critical Tab Tables (Vital stockouts & overstocks)
            renderCriticalTabs(data);

            // 5. Explorer Data Grid
            filterAndRender();
        }

        // Charts builder (Fanos minimalist palette)
        function renderCharts(stockStatusCounts, venCounts, data) {
            // Chart 1: Stock Status Doughnut (Semantic high-contrast colors)
            const ctxStatus = document.getElementById('chart-stock-status').getContext('2d');
            if (chartStockStatus) chartStockStatus.destroy();
            chartStockStatus = new Chart(ctxStatus, {
                type: 'doughnut',
                data: {
                    labels: ['Stockout (MOS=0)', 'Understocked (<3)', 'Adequate (3-6)', 'Overstocked (>6)'],
                    datasets: [{
                        data: [
                            stockStatusCounts['stockout'],
                            stockStatusCounts['understocked'],
                            stockStatusCounts['adequate'],
                            stockStatusCounts['overstocked']
                        ],
                        backgroundColor: [
                            '#ba1a1a',  // Shock Red
                            '#d97706',  // High-Vis Amber
                            '#10b981',  // Electric Green
                            '#171717'   // Jet Black
                        ],
                        borderColor: '#ffffff',
                        borderWidth: 2
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            position: 'bottom',
                            labels: {
                                color: '#1c1b1b',
                                font: { size: 9, family: 'Plus Jakarta Sans', weight: '500' },
                                boxWidth: 10
                            }
                        }
                    },
                    cutout: '70%'
                }
            });

            // Chart 2: VEN Breakdown (Pure clinical monochrome scale + accent)
            const ctxVen = document.getElementById('chart-ven').getContext('2d');
            if (chartVen) chartVen.destroy();
            chartVen = new Chart(ctxVen, {
                type: 'bar',
                data: {
                    labels: ['Vital (V)', 'Essential (E)', 'Non-Essential (N)', 'Local (L)'],
                    datasets: [{
                        data: [
                            venCounts['V'] || 0,
                            venCounts['E'] || 0,
                            venCounts['N'] || 0,
                            venCounts['L'] || 0
                        ],
                        backgroundColor: [
                            '#ba1a1a',  // Vital drug alerts highlighted in Shock Red
                            '#171717',  // Essential - Jet Black
                            '#747878',  // Non-Essential - Slate Gray
                            '#c4c7c7'   // Local - Light Outline Gray
                        ],
                        maxBarThickness: 28,
                        borderRadius: 4
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { display: false }
                    },
                    scales: {
                        y: {
                            grid: { color: '#ebe7e6' },
                            ticks: { color: '#747878', font: { size: 9, family: 'Plus Jakarta Sans' } }
                        },
                        x: {
                            grid: { display: false },
                            ticks: { color: '#1c1b1b', font: { size: 10, family: 'Plus Jakarta Sans', weight: '600' } }
                        }
                    }
                }
            });

            // Chart 3: Pipeline Funnel (Minimalist absolute values)
            let totalOrdered = 0;
            let totalShipped = 0;
            let totalDelivered = 0;
            data.forEach(item => {
                totalOrdered += item.ordered_qty;
                totalShipped += item.shipped_qty;
                totalDelivered += item.delivered_qty;
            });

            const ctxPipeline = document.getElementById('chart-pipeline').getContext('2d');
            if (chartPipeline) chartPipeline.destroy();
            chartPipeline = new Chart(ctxPipeline, {
                type: 'bar',
                data: {
                    labels: ['Ordered PO', 'Shipped Funnel', 'Completed Deliv.'],
                    datasets: [{
                        data: [totalOrdered, totalShipped, totalDelivered],
                        backgroundColor: [
                            '#171717',  // Jet Black
                            '#d97706',  // Amber
                            '#10b981'   // Green
                        ],
                        maxBarThickness: 32,
                        borderRadius: 4
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { display: false }
                    },
                    scales: {
                        y: {
                            grid: { color: '#ebe7e6' },
                            ticks: { color: '#747878', font: { size: 9, family: 'Plus Jakarta Sans' } }
                        },
                        x: {
                            grid: { display: false },
                            ticks: { color: '#1c1b1b', font: { size: 10, family: 'Plus Jakarta Sans', weight: '600' } }
                        }
                    }
                }
            });
        }

        // Render critical items exceptional audits
        function renderCriticalTabs(data) {
            // Tab 1: Critical Vital Stockouts (VEN=V and SOH=0, sorted by AMC desc)
            const vitalsStockout = data.filter(item => item.ven === 'V' && (item.soh === 0 || item.adj_mos === 0))
                .sort((a, b) => b.amc - a.amc);

            document.getElementById('critical-stockouts-total').textContent = `${vitalsStockout.length} Vital Drug Stockouts`;
            const tbody1 = document.getElementById('critical-vitals-tbody');
            tbody1.innerHTML = '';
            
            vitalsStockout.slice(0, 15).forEach(item => {
                const tr = document.createElement('tr');
                tr.className = 'hover:bg-fanos-surface-low transition-colors duration-100';
                
                let pipelineText = 'None';
                let pipelineClass = 'text-fanos-outline';
                if (item.shipped_qty > 0) {
                    pipelineText = `Shipped (${item.shipped_qty.toLocaleString()})`;
                    pipelineClass = 'text-fanos-warning font-semibold';
                } else if (item.ordered_qty > 0) {
                    pipelineText = `Ordered (${item.ordered_qty.toLocaleString()})`;
                    pipelineClass = 'text-black font-semibold';
                }

                tr.innerHTML = `
                    <td class="py-2.5 px-2 font-semibold text-black max-w-[240px] truncate" title="${item.item}">${item.item}</td>
                    <td class="py-2.5 px-2 text-center text-fanos-on-surface-variant font-medium">${item.unit || '-'}</td>
                    <td class="py-2.5 px-2 text-right font-bold text-black">${item.amc.toLocaleString(undefined, {maximumFractionDigits:0})}</td>
                    <td class="py-2.5 px-2 text-center text-xs ${pipelineClass}">${pipelineText}</td>
                `;
                tbody1.appendChild(tr);
            });
            if (vitalsStockout.length === 0) {
                tbody1.innerHTML = '<tr><td colspan="4" class="py-6 text-center text-fanos-outline">No vital drug outages detected globally.</td></tr>';
            }

            // Tab 2: Overstocked Vital Assets (VEN=V and AdjMOS > 12, sorted by AdjMOS desc)
            const vitalsOverstocked = data.filter(item => item.ven === 'V' && item.adj_mos > 12)
                .sort((a, b) => b.adj_mos - a.adj_mos);

            document.getElementById('overstocked-vitals-total').textContent = `${vitalsOverstocked.length} Overstocked Assets`;
            const tbody2 = document.getElementById('overstocked-vitals-tbody');
            tbody2.innerHTML = '';
            
            vitalsOverstocked.slice(0, 15).forEach(item => {
                const tr = document.createElement('tr');
                tr.className = 'hover:bg-fanos-surface-low transition-colors duration-100';
                
                tr.innerHTML = `
                    <td class="py-2.5 px-2 font-semibold text-black max-w-[240px] truncate" title="${item.item}">${item.item}</td>
                    <td class="py-2.5 px-2 text-center text-fanos-on-surface-variant font-medium">${item.unit || '-'}</td>
                    <td class="py-2.5 px-2 text-right font-bold text-black">${item.soh.toLocaleString(undefined, {maximumFractionDigits:0})}</td>
                    <td class="py-2.5 px-2 text-center font-bold text-fanos-warning">${item.adj_mos.toFixed(1)} MOS</td>
                `;
                tbody2.appendChild(tr);
            });
            if (vitalsOverstocked.length === 0) {
                tbody2.innerHTML = '<tr><td colspan="4" class="py-6 text-center text-fanos-outline">All vital inventories allocated efficiently.</td></tr>';
            }
        }

        // Render Regional Hub stock summary table (Fanos clinical grid layout)
        function renderHubSummaryTable(data) {
            const tbody = document.getElementById('hub-summary-tbody');
            tbody.innerHTML = '';
            
            // Calculate total national stock to compute capacity share
            let totalSOH = 0;
            data.forEach(item => { totalSOH += item.soh; });
            if (totalSOH === 0) totalSOH = 1;

            // Generate hub statistics
            const hubStats = hubNames.map(h => {
                let soh = 0;
                let stockouts = 0;
                let validItems = 0;
                
                data.forEach(item => {
                    if (item.item) {
                        validItems++;
                        const hubVal = item.hubs[h] || 0;
                        soh += hubVal;
                        if (hubVal === 0) {
                            stockouts++;
                        }
                    }
                });

                const stockoutRate = (stockouts / (validItems || 1)) * 100;
                const capacityShare = (soh / totalSOH) * 100;

                return { name: h, soh, stockoutRate, capacityShare };
            });

            // Sort hubs by stockout rate descending (so most troubled hubs show first)
            hubStats.sort((a, b) => b.stockoutRate - a.stockoutRate);

            hubStats.forEach(h => {
                const tr = document.createElement('tr');
                const isSelected = selectedHubName === h.name;
                tr.className = `hover:bg-fanos-surface-container cursor-pointer transition-all duration-150 ${isSelected ? 'bg-fanos-surface-high border-l-4 border-l-black font-semibold text-black' : ''}`;
                
                tr.addEventListener('click', () => {
                    selectedHubName = h.name;
                    // re-render the summary to show selection border
                    renderHubSummaryTable(data);
                    // update detail panel
                    updateHubDetailPanel(h.name, data);
                });

                // Capacity share single weight stroke bar
                const barColor = h.capacityShare > 10 ? 'bg-black' : 'bg-fanos-outline';

                tr.innerHTML = `
                    <td class="py-3 px-3 font-semibold text-black">${h.name}</td>
                    <td class="py-3 px-3 text-right font-mono font-medium">${h.soh.toLocaleString(undefined, {maximumFractionDigits:0})}</td>
                    <td class="py-3 px-3 text-right">
                        <span class="px-2 py-0.5 rounded text-[10px] font-extrabold uppercase ${h.stockoutRate > 60 ? 'badge-error' : 'badge-warning'}">
                            ${h.stockoutRate.toFixed(1)}% OUT
                        </span>
                    </td>
                    <td class="py-3 px-3 text-center">
                        <div class="flex items-center justify-center gap-2">
                            <div class="w-16 bg-fanos-surface-highest border border-fanos-outline-variant rounded-full h-1.5 overflow-hidden shrink-0">
                                <div class="h-full ${barColor}" style="width: ${Math.min(h.capacityShare * 3, 100)}%"></div>
                            </div>
                            <span class="text-[9px] text-fanos-outline w-6 text-right">${h.capacityShare.toFixed(1)}%</span>
                        </div>
                    </td>
                    <td class="py-3 px-3 text-center text-black hover:scale-110"><i class="fa-solid fa-angle-right"></i></td>
                `;
                tbody.appendChild(tr);
            });
        }

        // Update Selected Hub Detail Panel (Blueprint Gauges / Stark Paper theme)
        function updateHubDetailPanel(hubName, data) {
            document.getElementById('hub-detail-name').textContent = hubName;
            
            let soh = 0;
            let stockouts = 0;
            let vitalStockouts = [];
            
            data.forEach(item => {
                const hubVal = item.hubs[hubName] || 0;
                soh += hubVal;
                if (hubVal === 0) {
                    stockouts++;
                    if (item.ven === 'V') {
                        vitalStockouts.push(item);
                    }
                }
            });

            const totalItems = data.length || 1;
            const stockoutRate = (stockouts / totalItems) * 100;

            document.getElementById('hub-detail-soh').textContent = soh.toLocaleString(undefined, {maximumFractionDigits:0}) + ' Units';
            document.getElementById('hub-detail-stockout').textContent = `${stockoutRate.toFixed(1)}%`;
            document.getElementById('hub-detail-stockout-count-desc').textContent = `${stockouts} stocked out items (including ${vitalStockouts.length} Vital drugs):`;

            vitalStockouts.sort((a, b) => b.amc - a.amc);

            const listContainer = document.getElementById('hub-detail-stockouts-list');
            listContainer.innerHTML = '';

            vitalStockouts.slice(0, 8).forEach(item => {
                const div = document.createElement('div');
                div.className = 'p-2.5 bg-fanos-surface-lowest border border-fanos-surface-high rounded-[8px] flex items-center justify-between gap-3 text-xs';
                
                div.innerHTML = `
                    <div class="min-w-0">
                        <p class="font-bold text-black truncate" title="${item.item}">${item.item}</p>
                        <span class="body-small text-fanos-outline uppercase block">Unit: ${item.unit || '-'}</span>
                    </div>
                    <span class="shrink-0 px-1.5 py-0.5 rounded-[4px] badge-error font-extrabold text-[9px] uppercase">OUT</span>
                `;
                listContainer.appendChild(div);
            });

            if (vitalStockouts.length === 0) {
                listContainer.innerHTML = '<div class="py-8 text-center text-fanos-outline text-xs"><i class="fa-solid fa-face-smile text-emerald-600 text-lg mb-2 block"></i>No vital stockouts in this node!</div>';
            }
        }

        // Render Detailed Explorer Data Grid (Clean high legibility tabular layout)
        function renderExplorerTable(filteredItems) {
            const tbody = document.getElementById('explorer-tbody');
            tbody.innerHTML = '';

            const totalPages = Math.ceil(filteredItems.length / explorerPageSize) || 1;
            if (explorerPage > totalPages) explorerPage = totalPages;

            document.getElementById('table-row-count-showing').textContent = filteredItems.length.toLocaleString();
            document.getElementById('table-row-count-total').textContent = currentData.length.toLocaleString();
            document.getElementById('explorer-current-page').textContent = explorerPage;
            document.getElementById('explorer-total-pages').textContent = totalPages;

            // Enable/disable buttons
            document.getElementById('btn-prev-page').disabled = (explorerPage === 1);
            document.getElementById('btn-next-page').disabled = (explorerPage === totalPages);

            const startIdx = (explorerPage - 1) * explorerPageSize;
            const pageItems = filteredItems.slice(startIdx, startIdx + explorerPageSize);

            pageItems.forEach(item => {
                const tr = document.createElement('tr');
                tr.className = 'hover:bg-fanos-surface-low transition-colors duration-100';

                // Stock Status Badge
                let statusBadge = '';
                const mos = item.mos;
                if (mos === 0) {
                    statusBadge = '<span class="px-2 py-0.5 rounded-[4px] badge-error font-extrabold text-[9px] uppercase">Stockout</span>';
                } else if (mos < 3) {
                    statusBadge = '<span class="px-2 py-0.5 rounded-[4px] badge-warning font-extrabold text-[9px] uppercase">Understock</span>';
                } else if (mos <= 6) {
                    statusBadge = '<span class="px-2 py-0.5 rounded-[4px] badge-success font-extrabold text-[9px] uppercase">Adequate</span>';
                } else {
                    statusBadge = '<span class="px-2 py-0.5 rounded-[4px] badge-neutral font-extrabold text-[9px] uppercase">Overstock</span>';
                }

                // VEN Badge
                let venBadge = '';
                const v = item.ven;
                if (v === 'V') venBadge = '<span class="px-1.5 py-0.5 rounded-[4px] bg-black text-white font-black text-[9px]">V</span>';
                else if (v === 'E') venBadge = '<span class="px-1.5 py-0.5 rounded-[4px] bg-fanos-secondary text-white font-black text-[9px]">E</span>';
                else if (v === 'N') venBadge = '<span class="px-1.5 py-0.5 rounded-[4px] bg-fanos-surface-highest text-fanos-on-surface-variant font-bold text-[9px]">N</span>';
                else venBadge = `<span class="px-1.5 py-0.5 rounded-[4px] bg-fanos-outline text-white font-bold text-[9px]">${v}</span>`;

                // Pipeline Text
                let pipelineText = '<span class="text-fanos-outline">-</span>';
                if (item.shipped_qty > 0) {
                    pipelineText = `<span class="text-fanos-warning font-bold" title="PO: ${item.shipped_po}"><i class="fa-solid fa-ship mr-1 text-[10px]"></i>Ship (${item.shipped_qty.toLocaleString()})</span>`;
                } else if (item.ordered_qty > 0) {
                    pipelineText = `<span class="text-black font-bold" title="PO: ${item.ordered_po}"><i class="fa-solid fa-file-invoice-dollar mr-1 text-[10px]"></i>Order (${item.ordered_qty.toLocaleString()})</span>`;
                }

                tr.innerHTML = `
                    <td class="py-3.5 px-3 text-center text-fanos-outline font-mono">${item.sn || '-'}</td>
                    <td class="py-3.5 px-3 font-semibold text-black max-w-[280px] truncate" title="${item.item}">${item.item}</td>
                    <td class="py-3.5 px-3 text-center text-fanos-on-surface-variant font-medium">${item.unit || '-'}</td>
                    <td class="py-3.5 px-3 text-center">${venBadge}</td>
                    <td class="py-3.5 px-3 text-right font-mono font-bold text-black">${item.soh.toLocaleString(undefined, {maximumFractionDigits:0})}</td>
                    <td class="py-3.5 px-3 text-right font-mono text-fanos-on-surface-variant">${item.amc.toLocaleString(undefined, {maximumFractionDigits:0})}</td>
                    <td class="py-3.5 px-3 text-center font-mono">${item.mos.toFixed(1)}</td>
                    <td class="py-3.5 px-3 text-center font-mono font-bold text-black">${item.adj_mos.toFixed(1)}</td>
                    <td class="py-3.5 px-3 text-center">${pipelineText}</td>
                    <td class="py-3.5 px-3 max-w-[180px] truncate text-fanos-outline font-medium" title="${item.expiry}">${item.expiry || '<span class="text-fanos-surface-highest">-</span>'}</td>
                `;
                tbody.appendChild(tr);
            });

            if (filteredItems.length === 0) {
                tbody.innerHTML = '<tr><td colspan="10" class="py-12 text-center text-fanos-outline text-sm"><i class="fa-solid fa-circle-info text-2xl text-fanos-surface-highest mb-3 block"></i>No items found matching the selected search criteria and filters.</td></tr>';
            }
        }

        // Drag and Drop Excel Uploader Handler (dynamic calculations)
        function handleExcelUpload(e) {
            const file = e.target.files[0];
            if (!file) return;

            const reader = new FileReader();
            reader.onload = function(evt) {
                const data = evt.target.result;
                const workbook = XLSX.read(data, { type: 'binary' });
                
                // Read sheet 1
                const sheetName = workbook.SheetNames[0];
                const sheet = workbook.Sheets[sheetName];
                
                // Parse rows raw
                const rawRows = XLSX.utils.sheet_to_json(sheet, { header: 1 });
                if (rawRows.length < 3) {
                    alert('Excel sheet has insufficient rows. Must be in the standard EPSA Stock Report format.');
                    return;
                }

                // Process data rows starting from row 2
                const newItems = [];
                for (let r = 2; r < rawRows.length; r++) {
                    const row = rawRows[r];
                    if (!row || !row[1]) continue; // skip if item name is empty

                    // Column extraction helper matching python script mapping
                    const valAt = (idx) => {
                        const val = row[idx];
                        if (val === undefined || val === null) return 0;
                        const cleanStr = String(val).trim().replace(/,/g, '');
                        if (cleanStr === '' || cleanStr === '-' || cleanStr.toLowerCase() === 'none' || cleanStr.toLowerCase() === 'null') return 0;
                        const num = parseFloat(cleanStr);
                        return isNaN(num) ? 0 : num;
                    };

                    const strAt = (idx) => {
                        const val = row[idx];
                        return (val !== undefined && val !== null) ? String(val).trim() : '';
                    };

                    const hubs = {};
                    hubNames.forEach((h, index) => {
                        hubs[h] = valAt(26 + index);
                    });

                    const parsedItem = {
                        sn: row[0] || '',
                        item: strAt(1),
                        unit: strAt(2),
                        ven: strAt(3).toUpperCase() || 'UNKNOWN',
                        soh: valAt(4),
                        dos: valAt(5),
                        amc: valAt(6),
                        adj_amc: valAt(7),
                        mos: valAt(8),
                        adj_mos: valAt(9),
                        contract_qty: valAt(10),
                        contract_mos: valAt(11),
                        ordered_po: strAt(12),
                        ordered_qty: valAt(13),
                        ordered_mos: valAt(14),
                        shipped_po: strAt(15),
                        shipped_qty: valAt(16),
                        shipped_mos: valAt(17),
                        delivered_po: strAt(18),
                        delivered_qty: valAt(19),
                        delivered_mos: valAt(20),
                        left_qty: valAt(21),
                        left_mos: valAt(22),
                        expiry: strAt(23),
                        center_soh: valAt(24),
                        git: valAt(25),
                        hubs: hubs
                    };

                    newItems.push(parsedItem);
                }

                if (newItems.length === 0) {
                    alert('Could not parse any valid item rows from the uploaded sheet.');
                    return;
                }

                // Update active dataset & redraw
                currentData = newItems;
                explorerPage = 1;
                
                // Show Alert
                const alertEl = document.getElementById('upload-success-alert');
                alertEl.classList.remove('hidden');
                
                renderDashboard(currentData);
            };
            reader.readAsBinaryString(file);
        }
    </script>
</body>
</html>
"""

    # 3. Inject the parsed JSON data string
    html_content = html_content.replace('__INITIAL_DATA_PLACEHOLDER__', json_data_str)

    # 4. Write out the dashboard file
    output_path = 'Stock_Status_Dashboard.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Successfully compiled Stock_Status_Dashboard.html in workspace.")

if __name__ == '__main__':
    build_dashboard()
