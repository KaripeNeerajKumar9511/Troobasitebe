DEFAULT_NAV = [
    {"label": "How It Works", "href": "/how-it-works", "current": "how-it-works"},
    {"label": "Case Studies", "href": "/proof", "current": "proof", "mobileLabel": "Proof"},
    {"label": "Blogs", "href": "/blog", "current": "blog"},
    {"label": "About", "href": "/about", "current": "about"},
    {"label": "Solutions", "href": "/solutions", "current": "solutions"},
    {"label": "AI Capabilities", "href": "/ai-capabilities", "current": "ai-capabilities"},
]

DEFAULT_FOOTER = {
    "tagline": "Factory Flow Intelligence. Software that shows manufacturers how work actually moves through their factories.",
    "columns": [
        {
            "heading": "Trooba Flow",
            "links": [
                {"label": "How it works", "href": "/how-it-works"},
                {"label": "Solutions", "href": "/solutions"},
                {"label": "AI Capabilities", "href": "/ai-capabilities"},
                {"label": "Proof", "href": "/proof"},
                {"label": "Blogs", "href": "/blog"},
                {"label": "Request a Flow Analysis", "href": "/flow-analysis"},
            ],
        },
        {
            "heading": "Company",
            "links": [
                {"label": "About", "href": "/about"},
                {"label": "Contact", "href": "/contact"},
                {"label": "LinkedIn", "href": "https://www.linkedin.com/company/trooba", "external": True},
                {"label": "Privacy", "href": "/privacy"},
                {"label": "Terms", "href": "/terms"},
            ],
        },
    ],
    "copyright": "© 2026 Trooba. All Rights Reserved.\nTrooba is owned and operated by\nTechsprout AI Labs Private Limited.",
}

DEFAULT_TYPOGRAPHY = {
    "googleFontsHref": "https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600&family=DM+Mono:wght@400;500&display=swap",
    "fontSans": '"DM Sans", ui-sans-serif, system-ui, sans-serif',
    "fontMono": '"DM Mono", ui-monospace, monospace',
    "fs": {
        "display": "44px",
        "h1": "32px",
        "h2": "24px",
        "h3": "19px",
        "bodyLg": "17px",
        "body": "15px",
        "sm": "14px",
        "meta": "13px",
        "micro": "12px",
        "valueLg": "32px",
        "value": "15px",
        "valueSm": "13px",
    },
    "mk": {
        "hero": "clamp(2.5rem, 5.6vw, 4.25rem)",
        "section": "clamp(2rem, 3.8vw, 3rem)",
        "h3": "clamp(1.3125rem, 1.6vw, 1.5rem)",
        "lead": "clamp(1.0625rem, 1.25vw, 1.1875rem)",
        "body": "17px",
    },
}

DEFAULT_SEO = {
    "siteTitle": "AI-Powered Factory Flow Intelligence for Manufacturing | Trooba Flow",
    "siteDescription": "Trooba Flow helps manufacturers identify bottlenecks, reduce lead times, uncover hidden capacity, and test production changes before they affect the factory floor.",
    "ogImage": "/og-banner.png",
}

DEFAULT_LOGO = "/assets/logo/trooba-flow-light.svg"

CONTACT_FIELDS = {
    "label": "Trooba Flow™ Factory Flow Assessment",
    "h1": "We're selective. Intentionally.",
    "lead": "We run a structured pilot with manufacturers who have complex operations and a genuine appetite to understand their system.",
    "nextHeading": "What happens next",
    "steps": [
        {"title": "1  Review", "body": "We review your submission within 2 business days."},
        {"title": "2  Fit call", "body": "If there's a fit: a 60-minute call about your operation."},
        {"title": "3  Walkthrough", "body": "We walk through a Trooba Flow analysis using your factory context."},
    ],
    "formTitle": "Send the details",
    "formSubtitle": "Five fields. We will ask for the data itself after we have replied.",
    "labels": {
        "name": "Name",
        "email": "Work email",
        "company": "Company",
        "role": "Role",
        "roleOptional": "(optional)",
        "problem": "What is going wrong",
    },
    "placeholders": {
        "role": "Plant manager, operations, engineering",
        "problem": "Late orders on a particular family, lead time that will not come down, a capacity decision you are about to make.",
    },
    "problemHint": "Plain description is fine. We would rather have the symptom than a diagnosis.",
    "submitLabel": "Request a Flow Analysis",
    "submittingLabel": "Submitting...",
    "successMessage": "We'll personally review your request and follow up with the essentials for your product family.",
    "loginHtml": "Already have an account?",
    "loginHref": "https://app.trooba.com",
    "loginLabel": "Login.",
    "privacyNote": "We use this to reply to you and for nothing else. See the privacy notice.",
}

FLOW_FIELDS = {
    "h1": "Request a Flow Analysis",
    "lead": "We model one product family from data you already have, and show you where the queues form, what they cost in lead time, and which change moves them.",
    "nextHeading": "What happens Next..",
    "steps": [
        {
            "title": "1  Submit your details",
            "body": "Tell us about your company, production environment, current challenges, and priorities. The form helps us understand your operation before we reach out.",
        },
        {
            "title": "2  We review your operation",
            "body": "Our team reviews your responses to understand your production environment, operational challenges, and the information available to get started.",
        },
        {
            "title": "3  We follow up",
            "body": "We'll reach out to confirm a few details, answer any questions, and understand what you want to investigate first.",
        },
        {
            "title": "4  We start the analysis",
            "body": "Once we have what we need, we'll use your production information to build the initial model and identify where the biggest opportunities or constraints may be.",
        },
    ],
    "formTitle": "Send the details",
    "formSubtitle": "Eight steps. We will follow up after we have reviewed your submission.",
    "submitLabel": "Request Access",
    "submittingLabel": "Submitting...",
    "successMessage": "We'll be in touch within 2 business days.",
    "stepTitles": [
        "Basic Information",
        "Company Profile",
        "Manufacturing Environment",
        "Operational Challenges · 1",
        "Operational Challenges · 2",
        "Current Planning Process",
        "Data Availability",
        "Business Objectives",
    ],
    "options": {
        "industry": [
            "Packaging",
            "Electronics",
            "Industrial Equipment",
            "Automotive",
            "Aerospace",
            "Medical Devices",
            "Consumer Products",
            "Other",
        ],
        "revenue": ["<$10M", "$10M–50M", "$50M–250M", "$250M–1B", ">$1B"],
        "employees": ["<50", "50–200", "200–500", "500+"],
        "routingPaths": ["<10", "10–50", "50–200", "200+"],
        "sharedEquipment": ["Always", "Frequently", "Occasionally", "Rarely"],
        "scheduleChange": ["Multiple times per day", "Daily", "Weekly", "Rarely"],
        "erp": [
            "SAP",
            "Microsoft Dynamics",
            "Oracle",
            "Epicor",
            "Infor",
            "Odoo",
            "Other",
            "None",
        ],
        "schedulingMethod": ["ERP", "APS", "Excel", "Whiteboard", "Experience only"],
        "metrics": [
            "Throughput",
            "OEE",
            "Utilization",
            "WIP",
            "Lead Time",
            "On-Time Delivery",
            "Inventory",
            "None",
        ],
        "priorities": [
            "Reduce Lead Time",
            "Improve On-Time Delivery",
            "Reduce WIP",
            "Increase Throughput",
            "Delay Capital Investment",
            "Improve Capacity Planning",
            "Improve Quoting Accuracy",
            "Better Production Visibility",
            "Reduce Firefighting",
            "Improve Profitability",
        ],
        "challenges": [
            {"key": "expediteOrders", "label": "We frequently expedite orders."},
            {
                "key": "longLeadTimes",
                "label": "Customer lead times are longer than we would like.",
            },
            {
                "key": "highWip",
                "label": "Work-in-process inventory is higher than desired.",
            },
            {
                "key": "movingBottlenecks",
                "label": "Bottlenecks move between departments.",
            },
            {
                "key": "unevenResourceLoad",
                "label": "Some resources are overloaded while others remain idle.",
            },
            {
                "key": "changingPriorities",
                "label": "Production priorities change frequently.",
            },
            {
                "key": "unpredictableDelivery",
                "label": "We struggle to predict realistic delivery dates.",
            },
            {
                "key": "difficultCapacityPlanning",
                "label": "Capacity planning is difficult.",
            },
            {
                "key": "missDeliveriesDespiteUtilization",
                "label": "We have good equipment utilization but still miss deliveries.",
            },
            {
                "key": "overtimeToMeetCommitments",
                "label": "We often add overtime to meet commitments.",
            },
            {
                "key": "unsureBiggestImpact",
                "label": "We are unsure which improvement project will have the biggest impact.",
            },
        ],
    },
}

TEAM_SEED = [
    {
        "name": "Raghu Gidda",
        "role": "(Founder)",
        "photo_url": "/assets/Team_images/RaghuG.png",
        "alt": "Raghu Gidda, founder of Trooba",
    },
    {
        "name": "Vishwanath Srirangam",
        "role": "(Chief Technical Architect)",
        "photo_url": "/assets/Team_images/Vish.png",
        "alt": "Vishwanath Srirangam, Chief Technical Architect of Trooba",
    },
    {
        "name": "Shakti Sharma",
        "role": "(Business Development Manager)",
        "photo_url": "/assets/Team_images/Shakthi.png",
        "alt": "Shakti Sharma, Business Development Manager of Trooba",
    },
    {
        "name": "Raviteja Vasa",
        "role": "(Marketing Manager)",
        "photo_url": "/assets/Team_images/raviteja.jpeg",
        "alt": "Raviteja Vasa, Marketing Manager of Trooba",
    },
    {
        "name": "Karipe Neeraj Kumar",
        "role": "(Lead Technology Engineer)",
        "photo_url": "/assets/Team_images/Neeraj.png",
        "alt": "Karipe Neeraj Kumar, Lead Technology Engineer of Trooba",
    },
    {
        "name": "Sai Varun Somi Setty",
        "role": "(Lead Technology Engineer)",
        "photo_url": "/assets/Team_images/Varun.png",
        "alt": "Sai Varun Somi Setty, Lead Technology Engineer of Trooba",
    },
    {
        "name": "Guntuku Akanksha",
        "role": "(People Operational Manager)",
        "photo_url": "/assets/Team_images/Akanksha.jpeg",
        "alt": "Guntuku Akanksha, People Operational Manager of Trooba",
    },
    {
        "name": "SURAJ D KAMMAR",
        "role": "(Industrial Engineering Specialist)",
        "photo_url": "/assets/Team_images/suraj.png",
        "alt": "Suraj D Kammar, IE Specialist of Trooba",
    },
]

CASE_SEED = [
    {
        "slug": "tarinika",
        "title": "Tarinika",
        "badge": "Case 01",
        "status": "Completed · Measured result",
        "metric": "28 → 7 days",
        "caption": "> 75% reduction in manufacturing lead time",
        "image_url": "/Tarinika.png",
        "image_alt": "Factory floor at Tarinika",
        "facts": [
            {
                "dt": "The factory",
                "dd": "Jewellery manufacturer. Multi-SKU, make-to-order, several hundred active SKUs.",
            },
            {
                "dt": "The problem",
                "dd": "Manufacturing lead time of about four weeks, order to ship, while production capacity was available. Adding capacity had not fixed it.",
            },
            {
                "dt": "What the analysis revealed",
                "dd": "The constraint was not machine speed or nominal capacity. Lot sizing and queue dynamics were driving lead time.",
            },
            {
                "dt": "What changed",
                "dd": "Lot sizing and the way work was released and moved through the system. Same factory, same machines.",
            },
            {
                "dt": "Result",
                "dd": "Make-to-ship reduced from 28 days to 7 days — a reduction of more than 75%.",
            },
        ],
    },
    {
        "slug": "packaging",
        "title": "High-mix packaging manufacturer",
        "badge": "Case 02",
        "status": "In progress · Modelled scenario",
        "metric": "",
        "caption": "Modelled scenario, not a measured outcome.",
        "image_url": "/packing.png",
        "image_alt": "Packaging line model for a high-mix manufacturer",
        "facts": [],
    },
]

SOLUTION_SEED = [
    {
        "title": "Reduce Manufacturing Lead Time",
        "body": "See where time is really being lost across processing, equipment queues, labour queues, batching and variability.",
        "tagline": "Find the delays. Fix the flow.",
    },
    {
        "title": "Find Hidden Bottlenecks",
        "body": "Identify constraints that utilisation reports miss — including moving bottlenecks caused by mix, variability and shared resources.",
        "tagline": "See the constraint before it becomes a delivery problem.",
    },
    {
        "title": "Cut WIP and Queues",
        "body": "Understand why work accumulates between operations and which changes actually shrink queues.",
        "tagline": "Reduce waiting without starving production.",
    },
    {
        "title": "Make Better Capacity Decisions",
        "body": "Test whether you need more machines, more shifts, or a different release and routing policy.",
        "tagline": "Know when to add capacity — and when not to.",
    },
    {
        "title": "Improve On-Time Delivery",
        "body": "Connect queue behaviour to realistic dates instead of quoting from hope and tribal knowledge.",
        "tagline": "Improve delivery by fixing the causes upstream.",
    },
    {
        "title": "Test Changes Before the Shop Floor",
        "body": "Run demand, lot-size, routing and shift scenarios against the same model before you spend.",
        "tagline": "Test the decision before changing the factory.",
    },
]

PAGE_FILES = {
    "home": ("home.ts", "Home"),
    "how-it-works": ("howItWorks.ts", "How it works"),
    "proof": ("proof.ts", "Proof"),
    "about": ("about.ts", "About"),
    "solutions": ("solutions.ts", "Solutions"),
    "ai-capabilities": ("aiCapabilities.ts", "AI Capabilities"),
    "privacy": ("privacy.ts", "Privacy"),
    "terms": ("terms.ts", "Terms"),
}

BLOG_SEED = [
    {
        "slug": "why-high-utilization-increases-lead-time",
        "title": "Why high machine utilization can increase manufacturing lead time",
        "dek": "High machine utilization increases lead time by inflating queue time. Above roughly 85% utilization, waiting stops rising gently and starts rising steeply.",
        "category": "Manufacturing insights",
        "author": "Trooba Team",
        "published_at": "2026-08-31",
        "read_time": "8 min read",
        "sort_order": 0,
        "cover_url": "/assets/blog_imgs/why-high-utilization-increases-lead-time.png",
        "cover_alt": "Factory floor with machines running at high utilisation while jobs wait in queue",
        "seo": {
            "title": "High Machine Utilization Increases Lead Time | Trooba Flow",
            "description": "High machine utilization increases manufacturing lead time by inflating queue time. See the queueing math, a worked example, and how to set a better target.",
            "keywords": "high machine utilization, manufacturing lead time, queue time, Kingman's formula, Little's Law, Manufacturing Critical-Path Time, capacity utilization, work in process",
            "canonical": "https://trooba.com/blog/why-high-utilization-increases-lead-time",
            "ogTitle": "High Machine Utilization Increases Lead Time | Trooba Flow",
            "ogDescription": "High machine utilization increases manufacturing lead time by inflating queue time. See the queueing math, a worked example, and how to set a better target.",
            "ogUrl": "https://trooba.com/blog/why-high-utilization-increases-lead-time",
            "ogImage": "/assets/blog_imgs/why-high-utilization-increases-lead-time.png",
        },
    },
    {
        "slug": "manufacturing-lead-time-waiting-not-processing",
        "title": "Why most manufacturing lead time is waiting, not processing",
        "dek": "A part that takes four hours of real work routinely takes four weeks to reach the customer. The gap isn't slow machines — it's queue time, and it follows predictable mathematics.",
        "category": "Manufacturing insights",
        "author": "Trooba Team",
        "published_at": "2026-08-31",
        "read_time": "7 min read",
        "sort_order": 1,
        "cover_url": "/assets/blog_imgs/manufacturing-lead-time-waiting-not-processing.png",
        "cover_alt": "Parts waiting between operations while only a small share of lead time is processing",
        "seo": {
            "title": "Why Manufacturing Lead Time Is Mostly Waiting | Trooba Flow",
            "description": "Most manufacturing lead time is queue time, not processing time. Learn where the waiting hides, how to measure it, and which levers actually cut it.",
            "keywords": "manufacturing lead time, queue time, work in process, Little's Law, Manufacturing Critical-Path Time, machine utilisation, transfer lot size, high-mix low-volume manufacturing",
            "canonical": "https://trooba.com/blog/manufacturing-lead-time-waiting-not-processing",
            "ogTitle": "Why Manufacturing Lead Time Is Mostly Waiting | Trooba Flow",
            "ogDescription": "Most manufacturing lead time is queue time, not processing time. Learn where the waiting hides, how to measure it, and which levers actually cut it.",
            "ogUrl": "https://trooba.com/blog/manufacturing-lead-time-waiting-not-processing",
            "ogImage": "/assets/blog_imgs/manufacturing-lead-time-waiting-not-processing.png",
        },
    },
    {
        "slug": "manufacturing-critical-path-time-mct",
        "title": "Manufacturing Critical-Path Time (MCT): a better way to measure lead time",
        "dek": "MCT counts every calendar day an order truly takes — weekends, waiting, approvals, outside processing — from order entry to first piece delivered.",
        "category": "Manufacturing insights",
        "author": "Trooba Team",
        "published_at": "2026-08-31",
        "read_time": "8 min read",
        "sort_order": 2,
        "cover_url": "/assets/blog_imgs/manufacturing-critical-path-time-mct.png",
        "cover_alt": "Manufacturing Critical-Path Time map showing calendar days from order to first piece",
        "seo": {
            "title": "Manufacturing Critical-Path Time (MCT) Explained | Trooba",
            "description": "Manufacturing Critical-Path Time (MCT) measures the calendar days an order truly takes, from order entry to first piece shipped. Learn to map and reduce it.",
            "keywords": "manufacturing critical-path time, MCT, lead time measurement, Quick Response Manufacturing, QRM, queue time, touch time, work in process",
            "canonical": "https://trooba.com/blog/manufacturing-critical-path-time-mct",
            "ogTitle": "Manufacturing Critical-Path Time (MCT) Explained | Trooba",
            "ogDescription": "Manufacturing Critical-Path Time (MCT) measures the calendar days an order truly takes, from order entry to first piece shipped. Learn to map and reduce it.",
            "ogUrl": "https://trooba.com/blog/manufacturing-critical-path-time-mct",
            "ogImage": "/assets/blog_imgs/manufacturing-critical-path-time-mct.png",
        },
    },
    {
        "slug": "quick-response-manufacturing-qrm",
        "title": "What is Quick Response Manufacturing (QRM)?",
        "dek": "A factory can be busy all day and still be slow. QRM attacks calendar time — waiting, queues, WIP, and handoffs — rather than chasing machine utilisation.",
        "category": "Manufacturing insights",
        "author": "Trooba Team",
        "published_at": "2026-09-02",
        "read_time": "12 min read",
        "sort_order": 3,
        "cover_url": "/assets/blog_imgs/quick-response-manufacturing-qrm.png",
        "cover_alt": "Quick Response Manufacturing focuses on calendar time through cells, queues, and MCT",
        "seo": {
            "title": "Quick Response Manufacturing (QRM): A Practical Guide | Trooba",
            "description": "Learn what Quick Response Manufacturing (QRM) is, how it reduces manufacturing lead time, and how MCT, cells, capacity, and queues fit together.",
            "keywords": "Quick Response Manufacturing, QRM, manufacturing lead time, Manufacturing Critical-path Time, MCT, QRM cells, POLCA, queueing theory",
            "canonical": "https://trooba.com/blog/quick-response-manufacturing-qrm",
            "ogTitle": "Quick Response Manufacturing (QRM): A Practical Guide | Trooba",
            "ogDescription": "Learn what Quick Response Manufacturing (QRM) is, how it reduces manufacturing lead time, and how MCT, cells, capacity, and queues fit together.",
            "ogUrl": "https://trooba.com/blog/quick-response-manufacturing-qrm",
            "ogImage": "/assets/blog_imgs/quick-response-manufacturing-qrm.png",
        },
    },
    {
        "slug": "qrm-response-time-spiral",
        "title": "The QRM Response Time Spiral: why long lead times create even longer lead times",
        "dek": "Long manufacturing lead times encourage earlier release, more WIP, larger batches, and expediting — which grow queues and stretch lead time again.",
        "category": "Manufacturing insights",
        "author": "Trooba Team",
        "published_at": "2026-09-02",
        "read_time": "10 min read",
        "sort_order": 4,
        "cover_url": "/assets/blog_imgs/qrm-response-time-spiral.png",
        "cover_alt": "QRM Response Time Spiral showing how long lead times create more WIP and delay",
        "seo": {
            "title": "QRM Response Time Spiral: Why Lead Times Keep Growing | Trooba",
            "description": "Understand the QRM Response Time Spiral, why long manufacturing lead times create more WIP and queues, and how manufacturers can break the cycle.",
            "keywords": "QRM Response Time Spiral, manufacturing lead time, Quick Response Manufacturing, queue time, WIP, MCT, factory flow, manufacturing queues",
            "canonical": "https://trooba.com/blog/qrm-response-time-spiral",
            "ogTitle": "QRM Response Time Spiral: Why Lead Times Keep Growing | Trooba",
            "ogDescription": "Understand the QRM Response Time Spiral, why long manufacturing lead times create more WIP and queues, and how manufacturers can break the cycle.",
            "ogUrl": "https://trooba.com/blog/qrm-response-time-spiral",
            "ogImage": "/assets/blog_imgs/qrm-response-time-spiral.png",
        },
    },
]
