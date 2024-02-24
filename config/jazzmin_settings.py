JAZZMIN_SETTINGS = {

    # Login Page
    "site_header": "Dental.uz",

    "login_logo": "",

    "login_logo_dark": None,

    "welcome_sign": "Welcome to Dental Admin Panel",

    "site_brand": "Dental.uz",

    "site_logo": "admin/img/Posoxlogo2.png",

    "site_logo_classes": "img-fluid",

    "site_icon": "https://dental.uz/favicon.ico",

    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Support", "url": "", "new_window": True},
        {"model": "auth.User"},
        {"app": "reports"},
    ],

    "search_model": "auth.User",

    "usermenu_links": [
        {"name": "Support", "url": "", "new_window": True},
        {"model": "auth.accounts"}
    ],

    "site_title": "Dental Admin Panel",

    "copyright": "Ismailov Technologies",

    # The model admin to search from the search bar, search bar omitted if excluded

    # Field name on accounts model that contains avatar ImageField/URLField/Charfield or a callable that receives the accounts
    "user_avatar": None,
    "language_chooser": True,

    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": True,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.accounts)
    "hide_models": [],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": [
        "auth",
        "auth.token",
        "auth.Permission",
        "common.About",
        "common.ClinicMember",
        "common.Services",
        "common.Products",
        "common.Weekdays",
        "common.Weekends",
        "common.Contacts",
        "common.ApplicationForm",

    ],
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.Permission": "fas fa-key",
        "auth.User": "fas fa-user",
        "auth.Group": "fas fa-users",

        "common.About": "fas fa-clinic-medical",
        "common.ClinicMember": "fas fa-user-nurse",
        "common.Services": "fas fa-handshake",
        "common.Contacts": "fas fa-address-card",
        "common.Weekdays": "fas fa-calendar-alt",
        "common.Weekends": "fas fa-calendar-alt",
        "common.ApplicationForm": "fas fa-comments",
        "common.Products": "fas fa-box",

    },

    # Theme UI
    "theme": "darkly",

    # Custom links to append to app groups, keyed on app name
    "custom_links": {
        "books": [{
            "name": "Make Messages",
            "url": "make_messages",
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }]
    },

    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes

    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "collapsible",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.accounts": "collapsible", "auth.group": "vertical_tabs"},

}

JAZZMIN_UI_TWEAKS = {

    # "theme": "darkly",
    # "theme": "simplex",
    #  "theme": "sketchy",
    # "theme": "slate",
    "theme": "flatly",
    "dark_mode_theme": "darkly",
}
