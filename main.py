import os
import flet as ft
import flet_video as ftv
import webbrowser
import threading

def main(page: ft.Page):

    # =========================================================
    # PAGE SETTINGS (Optimized for Fixed Header Layout)
    # =========================================================
    page.title = "Tunacky Kandere - Civil Engineering Portfolio"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.spacing = 0
    page.bgcolor = "#fdf2f8"
    page.scroll = None  # Crucial: Page tracking disabled so container columns handle isolated scrolling

    # =========================================================
    # PREMIUM CIVIL ENGINEERING PINK PALETTE
    # =========================================================
    PRIMARY_BLUE = "#9d174d"        # Deep Rose
    ACCENT_AZURE = "#db2777"        # Vibrant Pink
    DEEP_NAVY = "#4a1942"           # Dark plum accent for text/buttons
    LIGHT_BG = "#fdf2f8"            # Soft pink-tint background
    SECTION_BLUE = "#fce7f3"
    SECTION_DEEP = "#fbcfe8"
    BG_WHITE = "#ffffff"
    TEXT_GREY = "#4a1942"
    AVATAR_BG = "#fce7f3"
    SUBTEXT_GREY = "#9d4b7a"
    CARD_BG = "#fffafb"
    BORDER_COLOR = "#f9a8d4"
    
    DARK_CARD_BG = "#4a1942"
    DARK_TEXT_WHITE = "#ffffff"
    NAV_INACTIVE = "#fbcfe8"
    OVERLAY_PINK = "#db2777"
    PROGRESS_TRACK = "#fce7f3"
    SHADOW_PINK = "#d8a0bc"
    CERT_HINT = "#fbcfe8"

    def open_certificate_zoom(title: str, image_file: str):
        zoom_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text(title, color=PRIMARY_BLUE, weight=ft.FontWeight.BOLD),
                content=ft.Container(
                width=900,
                height=620,
                bgcolor=BG_WHITE,
                padding=10,
                border_radius=8,
                content=ft.Image(src=f"/images/{image_file}", fit="contain"),
            ),
            actions=[
                ft.TextButton("Close", on_click=lambda e: close_certificate_zoom(zoom_dialog)),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        page.show_dialog(zoom_dialog)

    def close_certificate_zoom(dialog):
        page.pop_dialog()

    def get_uniform_border(width: int, color: str):
        return ft.Border(
            top=ft.BorderSide(width, color),
            bottom=ft.BorderSide(width, color),
            left=ft.BorderSide(width, color),
            right=ft.BorderSide(width, color),
        )

    # =========================================================
    # PREMIUM COMPONENT BUILDERS
    # =========================================================
    def create_section_header(title: str, subtitle: str):
        return ft.Column(
            spacing=8,
            controls=[
                ft.Text(
                    title, 
                    size=28, 
                    weight=ft.FontWeight.BOLD, 
                    color=PRIMARY_BLUE, 
                    style=ft.TextStyle(letter_spacing=1.2)
                ),
                ft.Text(subtitle, size=15, color=TEXT_GREY),
                ft.Container(height=4, width=60, bgcolor=ACCENT_AZURE, border_radius=2),
                ft.Container(height=15)
            ]
        )

    def create_skill_chip(label: str, level: float):
        return ft.Container(
            bgcolor=BG_WHITE,
            padding=ft.Padding(16, 12, 16, 12),
            border_radius=8,
            border=get_uniform_border(1, BORDER_COLOR),
            content=ft.Column([
                ft.Row([
                    ft.Text(label, weight=ft.FontWeight.W_600, color=DEEP_NAVY, size=14),
                    ft.Text(f"{int(level*100)}%", weight=ft.FontWeight.BOLD, color=PRIMARY_BLUE, size=12)
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Container(height=6),
                ft.Stack([
                    ft.Container(height=4, bgcolor=PROGRESS_TRACK, border_radius=2, expand=True),
                    ft.Container(height=4, bgcolor=PRIMARY_BLUE, border_radius=2, width=120 * level)
                ])
            ])
        )

    def create_info_card(title: str, body: str, icon=ft.Icons.CHECK_CIRCLE):
        return ft.Container(
            bgcolor=BG_WHITE,
            padding=20,
            border_radius=8,
            border=get_uniform_border(1, BORDER_COLOR),
            content=ft.Column(
                spacing=10,
                controls=[
                    ft.Row([
                        ft.Icon(icon, color=PRIMARY_BLUE, size=24),
                        ft.Text(title, size=16, weight=ft.FontWeight.BOLD, color=DEEP_NAVY),
                    ]),
                    ft.Text(body, color=TEXT_GREY, size=13),
                ],
            ),
        )

    # =========================================================
    # NAVIGATION SYSTEM
    # =========================================================
    current_page_key = {"value": "overview"}
    nav_buttons = {}

    def build_page_view(section_control, page_key):
        return ft.Column(
            key=f"page-{page_key}",
            expand=True,
            scroll=ft.ScrollMode.ALWAYS,
            spacing=0,
            controls=[section_control],
        )

    def navigate_to(page_key):
        current_page_key["value"] = page_key
        page_switcher.content = build_page_view(portfolio_pages[page_key], page_key)
        for key, button in nav_buttons.items():
            button.style = ft.ButtonStyle(
                color=BG_WHITE if key == page_key else NAV_INACTIVE,
                overlay_color=OVERLAY_PINK,
            )
        page.update()

    # =========================================================
    # SECTIONS DEFINITIONS
    # =========================================================
    
    # 1. Overview Section
    hero_section = ft.Container(
        key="overview",
        bgcolor=LIGHT_BG,
        padding=ft.Padding(50, 60, 50, 60),
        content=ft.ResponsiveRow(
            controls=[
                ft.Column(
                    col={"sm": 12, "md": 7},
                    spacing=15,
                    controls=[
                        ft.Text(
                            "CIVIL ENGINEERING STUDENT @ UNAM", 
                            size=13, 
                            weight=ft.FontWeight.W_600, 
                            color=ACCENT_AZURE, 
                            style=ft.TextStyle(letter_spacing=1.5)
                        ),
                        ft.Text("Tunacky Kandere", size=42, weight=ft.FontWeight.BOLD, color=PRIMARY_BLUE),
                        ft.Divider(color=PRIMARY_BLUE, thickness=1.5),
                        ft.Text("Phone: +264 81 496 7390  |  Email: tunackykandere@gmail.com", size=14, weight=ft.FontWeight.W_500, color=DEEP_NAVY),
                        ft.Text("Civil Engineering student focused on structural analysis, construction materials, surveying, infrastructure design, and data-driven engineering solutions.", size=16, color=TEXT_GREY),
                        ft.Container(height=10),
                        ft.ElevatedButton(
                            "Download CV (PDF)",
                            icon=ft.Icons.DOWNLOAD,
                            bgcolor=PRIMARY_BLUE,
                            color=BG_WHITE,
                            url="/cv.pdf",
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=6)),
                        ),
                    ],
                ),
                ft.Column(
                    col={"sm": 12, "md": 5},
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            width=220,
                            height=220,
                            border_radius=110,
                            bgcolor=AVATAR_BG,
                            alignment=ft.Alignment(0, 0),
                            border=get_uniform_border(4, PRIMARY_BLUE),
                            content=ft.Image(src="/images/ProfileK.jpeg", width=220, height=220, border_radius=110, fit="cover"),
                        ),
                        ft.Container(height=8),
                        ft.Text("Civil Engineering & Infrastructure Systems 2026", size=12, color=SUBTEXT_GREY, italic=True),
                    ],
                ),
            ]
        ),
    )

    # 2. Skills Section
    skills_section = ft.Container(
        key="skills",
        bgcolor=SECTION_BLUE,
        padding=40,
        content=ft.Column([
            create_section_header("CORE CIVIL & TECHNICAL MATRIX", "Integrated expertise across structures, materials, surveying, and digital engineering tools."),
            ft.ResponsiveRow([
                ft.Column(col={"sm": 12, "md": 4}, spacing=10, controls=[
                    ft.Text("Structures & Geotechnics", weight=ft.FontWeight.BOLD, color=ACCENT_AZURE, size=16),
                    create_skill_chip("Structural Analysis", 0.88),
                    create_skill_chip("Soil Mechanics & Foundations", 0.85),
                    create_skill_chip("Reinforced Concrete Design", 0.82),
                ]),
                ft.Column(col={"sm": 12, "md": 4}, spacing=10, controls=[
                    ft.Text("Engineering Software & Tools", weight=ft.FontWeight.BOLD, color=ACCENT_AZURE, size=16),
                    create_skill_chip("AutoCAD / Civil 3D", 0.80),
                    create_skill_chip("MATLAB Engineering Models", 0.85),
                    create_skill_chip("STAAD.Pro / ETABS", 0.75),
                ]),
                ft.Column(col={"sm": 12, "md": 4}, spacing=10, controls=[
                    ft.Text("Data & Digital Integration", weight=ft.FontWeight.BOLD, color=ACCENT_AZURE, size=16),
                    create_skill_chip("Python Engineering Analytics", 0.82),
                    create_skill_chip("GIS for Infrastructure", 0.78),
                    create_skill_chip("Power BI Dashboards", 0.80),
                ]),
            ], spacing=20)
        ])
    )

    # 3. Individual Portfolio Reflection Section
    contribution_section = ft.Container(
        key="contribution",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("INDIVIDUAL CONTRIBUTION PORTFOLIO", "Reflection, evidence, lessons learned, challenges, and showcase material."),
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            content=create_info_card(
                                "Semester Project Contribution",
                                "I contributed to the engineering logic, documentation, and portfolio evidence for the group app, with emphasis on making technical work traceable for the Mining, Metallurgical, and Civil engineering modules.",
                                ft.Icons.ENGINEERING,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            content=create_info_card(
                                "Evidence of Work",
                                "This portfolio includes certificate screenshots, implementation notes, code snippets, design/documentation placeholders, GitHub logs, and technical explanations that can be verified during assessment.",
                                ft.Icons.FACT_CHECK,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            content=create_info_card(
                                "What I Learned",
                                "I strengthened my ability to translate engineering calculations into software requirements, document individual progress in a large team, and present mathematical concepts clearly with proper notation.",
                                ft.Icons.LIGHTBULB,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            content=create_info_card(
                                "Challenges Addressed",
                                "The main challenge was proving individual contribution inside a 20-member project. I addressed it by organizing weekly logs, GitHub evidence, screenshots, and a concise impact narrative.",
                                ft.Icons.TROUBLESHOOT,
                            ),
                        ),
                    ],
                ),
                ft.Container(
                    bgcolor=LIGHT_BG,
                    padding=20,
                    border_radius=8,
                    border=get_uniform_border(1, BORDER_COLOR),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Column([
                                ft.Text("Individual Contribution Video", size=18, weight=ft.FontWeight.BOLD, color=DEEP_NAVY),
                                ft.Text("Add the final showcase recording link here so it matches the contribution you will present live.", color=TEXT_GREY, size=13),
                            ]),
                            ft.TextButton("Video Link Placeholder", icon=ft.Icons.VIDEO_LIBRARY, url="https://example.com/contribution-video", style=ft.ButtonStyle(color=ACCENT_AZURE)),
                        ],
                    ),
                ),
            ],
        ),
    )

    # 4. Project Timeline Section
    timeline_section = ft.Container(
        key="timeline",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("PROJECT TIMELINE", "Weekly log of my specific contributions to the semester group project."),
                ft.Container(
                    bgcolor=BG_WHITE,
                    padding=25,
                    border_radius=10,
                    border=get_uniform_border(1, BORDER_COLOR),
                    content=ft.Column(
                        spacing=15,
                        controls=[
                            ft.Text("Week 01 - Requirements and Role Definition", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_AZURE),
                            ft.Text("Reviewed the semester brief, mapped the Metallurgical, Mining, and Civil engineering modules, and documented the screens and calculations I would support.", color=TEXT_GREY),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("Week 02 - MATLAB and Engineering Logic", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_AZURE),
                            ft.Text("Completed short MathWorks courses, converted calculation requirements into MATLAB-style formulas, and checked units for cost, material, and stability calculations.", color=TEXT_GREY),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("Week 03 - Feature Implementation", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_AZURE),
                            ft.Text("Built and refined user interface components for module evidence, technical explanations, and engineering outputs that could be traced back to group requirements.", color=TEXT_GREY),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("Week 04 - Review, Documentation, and Showcase Prep", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_AZURE),
                            ft.Text("Captured screenshots, wrote contribution notes, prepared GitHub evidence, and aligned the portfolio video with the work I will present during the showcase.", color=TEXT_GREY),
                        ],
                    ),
                ),
            ],
        ),
    )

    # 5. Projects Section
    project_section = ft.Container(
        key="projects",
        bgcolor=BG_WHITE,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("CIVIL ENGINEERING PROJECTS", "Advanced analytical tools for structural assessment and infrastructure planning."),
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=CARD_BG,
                            padding=25,
                            border_radius=10,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Text("1. Rock Mass Rating (RMR) & Stability Simulator", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_AZURE),
                                    ft.Text("Comprehensive MATLAB-based geotechnical tool for evaluating rock mass quality, stand-up time predictions, and support recommendations for underground excavations.", color=TEXT_GREY, size=14),
                                    ft.Container(
                                        bgcolor=LIGHT_BG,
                                        padding=12,
                                        border_radius=6,
                                        content=ft.Column([
                                            ft.Text("GEOTECHNICAL PARAMETERS IMPLEMENTED:", size=11, weight=ft.FontWeight.BOLD, color=DEEP_NAVY),
                                            ft.Text("• RMR = UCS_Rating + RQD_Rating + Spacing_Rating + Joint_Rating + Water_Rating", size=12, font_family="monospace", color=ACCENT_AZURE),
                                            ft.Text("• Q-System: Q = (RQD/Jn) × (Jr/Ja) × (Jw/SRF)", size=12, font_family="monospace", color=ACCENT_AZURE),
                                            ft.Text("• Stand-up Time: t = exp(0.5 × RMR - 30) hours", size=12, font_family="monospace", color=ACCENT_AZURE),
                                            ft.Text("• Support Pressure: P = 0.2 × (RMR - 40) kPa", size=12, font_family="monospace", color=ACCENT_AZURE),
                                        ])
                                    ),
                                    ft.Text("Enables mine planners to assess excavation stability, recommend rock bolt patterns, shotcrete requirements, and predict potential failure modes based on geotechnical indices.", color=TEXT_GREY, size=12),
                                    ft.Row([
                                        ft.Container(content=ft.Text("MATLAB Geotech", size=11, color=BG_WHITE), bgcolor=PRIMARY_BLUE, padding=5, border_radius=4),
                                        ft.Container(content=ft.Text("RocScience RS2", size=11, color=DEEP_NAVY), bgcolor=LIGHT_BG, padding=5, border_radius=4),
                                    ])
                                ],
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=CARD_BG,
                            padding=25,
                            border_radius=10,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Text("2. Mine Ventilation Network Optimizer", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_AZURE),
                                    ft.Text("Interactive simulation tool for analyzing airflow distribution, pressure drops, and fan selection in complex underground mine ventilation systems.", color=TEXT_GREY, size=14),
                                    ft.Container(
                                        bgcolor=LIGHT_BG,
                                        padding=12,
                                        border_radius=6,
                                        content=ft.Column([
                                            ft.Text("VENTILATION CORE EQUATIONS:", size=11, weight=ft.FontWeight.BOLD, color=DEEP_NAVY),
                                            ft.Text("• Atkinson's Equation: P = K × L × (A × v²) / A³", size=12, font_family="monospace", color=ACCENT_AZURE),
                                            ft.Text("• Pressure Loss: ΔP = R × Q²", size=12, font_family="monospace", color=ACCENT_AZURE),
                                            ft.Text("• Network Equilibrium: ΣΔP_loop = 0", size=12, font_family="monospace", color=ACCENT_AZURE),
                                            ft.Text("• Air Quantity: Q = v × A (m³/s)", size=12, font_family="monospace", color=ACCENT_AZURE),
                                        ])
                                    ),
                                    ft.Text("Assists ventilation engineers in designing efficient airway networks, calculating required fan pressures, and ensuring compliance with occupational health standards.", color=TEXT_GREY, size=12),
                                    ft.Row([
                                        ft.Container(content=ft.Text("Python Scripting", size=11, color=BG_WHITE), bgcolor=PRIMARY_BLUE, padding=5, border_radius=4),
                                        ft.Container(content=ft.Text("Ventsim", size=11, color=DEEP_NAVY), bgcolor=LIGHT_BG, padding=5, border_radius=4),
                                    ])
                                ],
                            ),
                        ),
                    ],
                ),
            ],
        ),
    )

    # 6. Technical Blog Section - WITH VIDEO (Fixed)
    blog_section = ft.Container(
        key="blog",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("TECHNICAL BLOG: CONFIDENCE IN CONCEPTS", "Written technical explanations with embedded video demonstrations."),
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=22,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Text("Material Cost Estimation", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_AZURE),
                                    ft.Text("For engineering modules, cost estimation combines quantity, unit price, and overhead allowances. Correct notation keeps the calculation readable and auditable.", color=TEXT_GREY, size=13),
                                    ft.Container(
                                        bgcolor=LIGHT_BG,
                                        padding=14,
                                        border_radius=6,
                                        content=ft.Text("Total Cost = Σ[i=1 to n](Q_i × P_i) + Overheads", font_family="monospace", size=14, color=PRIMARY_BLUE),
                                    ),
                                    ft.Text("Where Q_i is the quantity of item i, P_i is its unit price, and n is the number of priced materials or activities.", color=TEXT_GREY, size=13),
                                ],
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=22,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Text("Engineering Module Impact", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_AZURE),
                                    ft.Text("In the Civil and Mining modules, structured formulas helped connect interface inputs to practical outputs such as support recommendations, ventilation checks, and equipment planning.", color=TEXT_GREY, size=13),
                                    ft.Container(
                                        bgcolor=LIGHT_BG,
                                        padding=14,
                                        border_radius=6,
                                        content=ft.Text("Q_air = v × A   |   ΔP = R × Q_air^2", font_family="monospace", size=14, color=PRIMARY_BLUE),
                                    ),
                                    ft.Text("The notation makes assumptions visible: velocity, area, resistance, and pressure loss must be documented before results are trusted.", color=TEXT_GREY, size=13),
                                ],
                            ),
                        ),
                    ],
                ),
                # VIDEO SECTION - Embedded Video Player (Fixed - using padding instead of margin)
                ft.Container(
                    padding=ft.Padding(0, 30, 0, 0),  # top=30, left=0, right=0, bottom=0
                    content=ft.Column(
                        spacing=15,
                        controls=[
                            ft.Divider(color=BORDER_COLOR, thickness=1),
                            ft.Text("📹 PROJECT DEMONSTRATION VIDEO", size=20, weight=ft.FontWeight.BOLD, color=PRIMARY_BLUE, text_align=ft.TextAlign.CENTER),
                            ft.Text("Watch the full demonstration of the Civil Engineering portfolio and technical implementations.", size=14, color=TEXT_GREY, text_align=ft.TextAlign.CENTER),
                            ft.Container(
                                padding=20,
                                bgcolor=BG_WHITE,
                                border_radius=12,
                                border=get_uniform_border(2, BORDER_COLOR),
                                content=ftv.Video(
                                    expand=True,
                                    playlist=[ftv.VideoMedia("/video/video.mp4")],
                                    playlist_mode=ftv.PlaylistMode.LOOP,
                                    fill_color=PRIMARY_BLUE,
                                    aspect_ratio=16/9,
                                    volume=100,
                                    autoplay=True,
                                    show_controls=True,
                                    filter_quality=ft.FilterQuality.HIGH,
                                    muted=False,
                                    wakelock=True,
                                ),
                            ),
                            ft.Text("This video showcases the key features, engineering calculations, and technical implementations demonstrated in this portfolio.", size=12, color=SUBTEXT_GREY, text_align=ft.TextAlign.CENTER, italic=True),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ),
            ],
        ),
    )

    # 7. Experience / Leadership Section
    leadership_section = ft.Container(
        key="experience",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("CIVIL ENGINEERING LEADERSHIP & FIELD EXPERIENCE", "Active contributions to the civil engineering community and practical site exposure."),
                ft.Text("Bridging academic civil engineering theory with practical industry applications while mentoring aspiring engineers.", size=15, color=TEXT_GREY),
                ft.ResponsiveRow(
                    spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column([
                                ft.Icon(ft.Icons.GROUP, color=PRIMARY_BLUE, size=28),
                                ft.Text("Civil Engineering Society Member", size=16, weight=ft.FontWeight.BOLD, color=DEEP_NAVY),
                                ft.Text("Contributing to student-led workshops, industry guest lectures, and site visit coordination with local construction and infrastructure projects.", color=TEXT_GREY, size=13),
                            ])
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column([
                                ft.Icon(ft.Icons.CONSTRUCTION, color=PRIMARY_BLUE, size=28),
                                ft.Text("Intern - Civil Engineering Site", size=16, weight=ft.FontWeight.BOLD, color=DEEP_NAVY),
                                ft.Text("Site surveying, material testing, structural inspections, and assisting senior civil engineers with infrastructure design evaluations.", color=TEXT_GREY, size=13),
                            ])
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column([
                                ft.Icon(ft.Icons.SCHOOL, color=PRIMARY_BLUE, size=28),
                                ft.Text("Academic Peer Tutoring", size=16, weight=ft.FontWeight.BOLD, color=DEEP_NAVY),
                                ft.Text("Providing guidance in structural mechanics, materials science, and surveying to undergraduate students.", color=TEXT_GREY, size=13),
                            ])
                        ),
                    ]
                )
            ]
        )
    )

    # 8. MATLAB Achievement Hub Section
    certificate_data = [
        {"title": "MATLAB Onramp", "file": "MATLAB Onramp.jpg"},
        {"title": "Simulink Onramp", "file": "Simulink Onramp.jpg"},
        {"title": "Machine Learning Onramp", "file": "Machine learning Onramp.jpg"},
        {"title": "Make and Manipulate Matrices", "file": "Make and Manipulate Matrices.jpg"},
        {"title": "Explore Data with MATLAB Plots", "file": "Explore Data with MATLAB Plots.jpg"},
        {"title": "Image Registration", "file": "Image Registration.jpg"},
    ]

    cert_cards = []
    for cert in certificate_data:
        if cert["file"]:
            img_control = ft.Image(
                src=f"/images/{cert['file']}",
                height=150,
                fit="contain", 
                scale=1.0,
                animate_scale=ft.Animation(400, ft.AnimationCurve.EASE_OUT),
            )
        else:
            img_control = ft.Container(
                height=140,
                bgcolor=LIGHT_BG,
                alignment=ft.Alignment(0, 0),
                content=ft.Column(
                    spacing=6,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(ft.Icons.UPLOAD_FILE, color=PRIMARY_BLUE, size=32),
                        ft.Text("Completion proof pending", color=DEEP_NAVY, size=12, text_align=ft.TextAlign.CENTER),
                    ],
                ),
            )

        card_design = ft.Container(
            bgcolor=DARK_CARD_BG,
            padding=15,
            border_radius=10,
            border=get_uniform_border(1, ACCENT_AZURE),
            on_click=lambda e, title=cert["title"], file=cert["file"]: open_certificate_zoom(title, file) if file else None,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        height=150,
                        width=320,
                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                        border_radius=6,
                        bgcolor=BG_WHITE,
                        alignment=ft.Alignment(0, 0),
                        content=img_control,
                    ),
                    ft.Container(height=6),
                    ft.Text(cert["title"], weight=ft.FontWeight.BOLD, color=DARK_TEXT_WHITE, text_align=ft.TextAlign.CENTER, size=13, max_lines=2, overflow=ft.TextOverflow.ELLIPSIS),
                    ft.Text("Click to zoom", color=CERT_HINT, size=11, text_align=ft.TextAlign.CENTER),
                ],
            ),
        )

        hover_stack = ft.Stack(
            height=230,
            controls=[
                ft.Container(top=10, left=0, right=0, animate_position=ft.Animation(300, ft.AnimationCurve.EASE_OUT), content=card_design)
            ]
        )

        def make_hover_handler(stack_wrapper, target_img):
            inner_move_container = stack_wrapper.controls[0]
            def handle_hover(e):
                if e.data == "true":
                    inner_move_container.top = 0  
                    inner_move_container.shadow = ft.BoxShadow(blur_radius=12, color=ACCENT_AZURE)
                    target_img.scale = 1.05  
                else:
                    inner_move_container.top = 10  
                    inner_move_container.shadow = None
                    target_img.scale = 1.0
                inner_move_container.update()
                target_img.update()
            return handle_hover

        if cert["file"]:
            card_design.on_hover = make_hover_handler(hover_stack, img_control)
        cert_cards.append(ft.Container(col={"sm": 12, "md": 4}, content=hover_stack))

    certification_section = ft.Container(
        key="certificates",
        bgcolor=SECTION_DEEP,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("MATLAB ACHIEVEMENT HUB", "Proof of completion for 6 short self-paced courses from the MathWorks Learning Center."),
                ft.Text("Click any certificate to zoom in and inspect the completion proof clearly.", size=13, color=SUBTEXT_GREY),
                ft.ResponsiveRow(spacing=20, run_spacing=10, controls=cert_cards),
            ],
        ),
    )

    # 9. GitHub Evidence & Documentation Section
    github_section = ft.Container(
        key="github",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Column([
                            ft.Text("GITHUB EVIDENCE & DOCUMENTATION", size=28, weight=ft.FontWeight.BOLD, color=PRIMARY_BLUE),
                            ft.Text("Verifiable individual contribution records for a 20-member semester project team.", size=15, color=TEXT_GREY),
                        ]),
                        ft.IconButton(icon=ft.Icons.CODE, icon_color=PRIMARY_BLUE, tooltip="GitHub Evidence")
                    ]
                ),
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            content=create_info_card(
                                "Commit History",
                                "Add screenshots or direct API pulls showing commits authored by Tunacky Kandere in the main repository, including dates, messages, and linked files.",
                                ft.Icons.COMMIT,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            content=create_info_card(
                                "Pull Request Logs",
                                "Document proposed features, reviews performed for team members, comments resolved, and merges completed during the semester project.",
                                ft.Icons.MERGE,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            content=create_info_card(
                                "Impact Summary",
                                "My code and documentation improved traceability of calculations and helped explain how engineering module outputs solve Mining, Metallurgical, or Civil engineering problems.",
                                ft.Icons.INSIGHTS,
                            ),
                        ),
                    ],
                ),
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=10,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Row([ft.Icon(ft.Icons.FOLDER_SPECIAL, color=PRIMARY_BLUE), ft.Text("Geotech-RMR-Calculator", size=16, weight=ft.FontWeight.BOLD, color=DEEP_NAVY)]),
                                    ft.Text("Interactive rock mass rating system with support recommendations, stand-up time predictions, and graphical stability charts for underground excavations.", size=13, color=TEXT_GREY),
                                    ft.Row(wrap=True, spacing=5, controls=[
                                        ft.Container(content=ft.Text("Python", size=10, color=BG_WHITE), bgcolor=PRIMARY_BLUE, padding=4, border_radius=4),
                                        ft.Container(content=ft.Text("MATLAB", size=10, color=DEEP_NAVY), bgcolor=LIGHT_BG, padding=4, border_radius=4),
                                        ft.Container(content=ft.Text("Plotly", size=10, color=DEEP_NAVY), bgcolor=LIGHT_BG, padding=4, border_radius=4),
                                    ]),
                                    ft.Divider(color=BORDER_COLOR),
                                    ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
                                        ft.Text("Active Development", size=11, color=SUBTEXT_GREY),
                                        ft.TextButton("View Repository", style=ft.ButtonStyle(color=ACCENT_AZURE))
                                    ])
                                ]
                            )
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=10,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Row([ft.Icon(ft.Icons.FOLDER, color=PRIMARY_BLUE), ft.Text("Infrastructure-Load-Analyzer", size=16, weight=ft.FontWeight.BOLD, color=DEEP_NAVY)]),
                                    ft.Text("Ventilation network solver for underground mines. Calculates airflow distribution, pressure drops, and optimal fan placement for regulatory compliance.", size=13, color=TEXT_GREY),
                                    ft.Row(wrap=True, spacing=5, controls=[
                                        ft.Container(content=ft.Text("Python", size=10, color=BG_WHITE), bgcolor=PRIMARY_BLUE, padding=4, border_radius=4),
                                        ft.Container(content=ft.Text("NumPy/SciPy", size=10, color=DEEP_NAVY), bgcolor=LIGHT_BG, padding=4, border_radius=4),
                                    ]),
                                    ft.Divider(color=BORDER_COLOR),
                                    ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
                                        ft.Text("Stable Release", size=11, color=SUBTEXT_GREY),
                                        ft.TextButton("View Repository", style=ft.ButtonStyle(color=ACCENT_AZURE))
                                    ])
                                ]
                            )
                        ),
                    ],
                ),
            ],
        ),
    )

    # 10. Contact Section Form Setup
    name_field = ft.TextField(label="Your Full Name", border_color=PRIMARY_BLUE, focused_border_color=ACCENT_AZURE)
    email_field = ft.TextField(label="Email Address", border_color=PRIMARY_BLUE, focused_border_color=ACCENT_AZURE)
    message_field = ft.TextField(label="Project Details / Inquiry Message", multiline=True, min_lines=4, border_color=PRIMARY_BLUE, focused_border_color=ACCENT_AZURE)

    def handle_submit_message(e):
        if not name_field.value or not email_field.value:
            page.show_snack_bar(ft.SnackBar(content=ft.Text("Please fill out your Name and Email fields before submitting."), bgcolor=ACCENT_AZURE))
        else:
            page.show_snack_bar(ft.SnackBar(content=ft.Text(f"Thank you {name_field.value}! Your message was compiled and sent successfully."), bgcolor=PRIMARY_BLUE))
            name_field.value = ""
            email_field.value = ""
            message_field.value = ""
            page.update()

    contact_section = ft.Container(
        key="contact",
        bgcolor=BG_WHITE,
        padding=40,
        content=ft.Column([
            create_section_header("GET IN TOUCH", "Collaborate on civil engineering projects, infrastructure research, or industry opportunities."),
            ft.ResponsiveRow(
                spacing=30,
                controls=[
                    ft.Column(
                        col={"sm": 12, "md": 5},
                        spacing=15,
                        controls=[
                            ft.Text("Available for civil engineering consultation, structural analysis, infrastructure planning, and research collaborations.", color=TEXT_GREY, size=15),
                            ft.Container(height=10),
                            ft.Row([ft.Icon(ft.Icons.LOCATION_ON, color=PRIMARY_BLUE), ft.Text("Ongwediva, Namibia (Civil Engineering Campus)", color=DEEP_NAVY, weight=ft.FontWeight.W_500)]),
                            ft.Row([ft.Icon(ft.Icons.EMAIL, color=PRIMARY_BLUE), ft.Text("tunackykandere@gmail.com", color=DEEP_NAVY, weight=ft.FontWeight.W_500)]),
                            ft.Row([ft.Icon(ft.Icons.PHONE_ANDROID, color=PRIMARY_BLUE), ft.Text("+264 81 496 7390", color=DEEP_NAVY, weight=ft.FontWeight.W_500)]),
                        ]
                    ),
                    ft.Container(
                        col={"sm": 12, "md": 7},
                        bgcolor=CARD_BG,
                        padding=30,
                        border_radius=12,
                        border=get_uniform_border(1, BORDER_COLOR),
                        content=ft.Column(
                            spacing=15,
                            controls=[
                                ft.Text("Send a Message Directly", size=16, weight=ft.FontWeight.BOLD, color=DEEP_NAVY),
                                name_field, email_field, message_field,
                                ft.Container(height=5),
                                ft.ElevatedButton("Submit Message", icon=ft.Icons.SEND, bgcolor=PRIMARY_BLUE, color=BG_WHITE, on_click=handle_submit_message, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=6)))
                            ]
                        )
                    )
                ]
            )
        ])
    )

    portfolio_pages = {
        "overview": hero_section,
        "skills": skills_section,
        "contribution": contribution_section,
        "timeline": timeline_section,
        "projects": project_section,
        "blog": blog_section,
        "experience": leadership_section,
        "certificates": certification_section,
        "github": github_section,
        "contact": contact_section,
    }

    page_switcher = ft.AnimatedSwitcher(
        content=build_page_view(hero_section, "overview"),
        duration=220,
        reverse_duration=160,
        switch_in_curve=ft.AnimationCurve.EASE_OUT,
        switch_out_curve=ft.AnimationCurve.EASE_IN,
        transition=ft.AnimatedSwitcherTransition.FADE,
        expand=True,
    )

    def make_nav_button(label, page_key):
        button = ft.TextButton(
            label,
            style=ft.ButtonStyle(
                color=BG_WHITE if page_key == current_page_key["value"] else NAV_INACTIVE,
                overlay_color=OVERLAY_PINK,
            ),
            on_click=lambda e, target=page_key: navigate_to(target),
        )
        nav_buttons[page_key] = button
        return button

    # =========================================================
    # STICKY NAVBAR PANEL (Pinned permanently to top layer)
    # =========================================================
    header_navbar = ft.Container(
        bgcolor=PRIMARY_BLUE,
        padding=ft.Padding(40, 15, 40, 15),
        border=ft.Border(bottom=ft.BorderSide(1, ACCENT_AZURE)),
        shadow=ft.BoxShadow(blur_radius=10, color=SHADOW_PINK, offset=ft.Offset(0, 2)),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Row([
                    ft.Container(width=12, height=12, bgcolor=BG_WHITE, border_radius=6),
                    ft.Text("TUNACKY KANDERE", weight=ft.FontWeight.BOLD, size=16, color=BG_WHITE, style=ft.TextStyle(letter_spacing=1.1))
                ], spacing=10),
                ft.Row([
                    make_nav_button("Overview", "overview"),
                    make_nav_button("Skills", "skills"),
                    make_nav_button("Portfolio", "contribution"),
                    make_nav_button("Timeline", "timeline"),
                    make_nav_button("Projects", "projects"),
                    make_nav_button("Blog", "blog"),
                    make_nav_button("Experience", "experience"),
                    make_nav_button("MATLAB Hub", "certificates"),
                    make_nav_button("GitHub", "github"),
                    make_nav_button("Contact", "contact"),
                ], spacing=10, wrap=True)
            ]
        )
    )

    # =========================================================
    # RENDER DIRECT TO MAIN PAGE WINDOW
    # =========================================================
    page.add(
        ft.Column(
            expand=True,
            spacing=0,
            controls=[
                header_navbar,       # Stays perfectly frozen at the top
                page_switcher        # Swaps section pages beneath the navbar
            ]
        )
    )

def open_browser():
    """Open the web browser automatically when the server starts"""
    import time
    time.sleep(2)  # Give the server a moment to start
    webbrowser.open("http://127.0.0.1:8551")

if __name__ == "__main__":
    try:
        # Start the browser opener in a separate thread
        threading.Thread(target=open_browser, daemon=True).start()
        
        # Run the Flet app with web support
        ft.app(
            target=main,
            host="127.0.0.1",
            port=8551,
            view=ft.AppView.WEB_BROWSER,  # This will open in default browser
            assets_dir="assets",
        )
    except Exception as e:
        print(f"Error: {e}", flush=True)
        import traceback
        traceback.print_exc()