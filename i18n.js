const translations = {
    en: {
        // Navigation (already mostly working)
        nav_security_scan: "Security Scan",
        nav_full_scanner: "Full Scanner",
        nav_threat_feed: "Threat Feed",
        nav_scan_history: "Scan History",
        nav_security_vault: "Security Vault",
        nav_data_reports: "Data Reports",
        nav_account: "Account",
        nav_documentation: "Documentation",
        nav_support: "Support",
        nav_new_scan: "New Scan",
        
        // Dashboard (Exact matches for your screenshot)
        dash_title: "Deep Inspection",
        dash_subtitle: "Advanced heuristic analysis for mission-critical mail protection.",
        dash_engine_status: "Engine Status",
        dash_optimal_security: "Optimal Security",
        dash_heuristic_health: "Heuristic Health",
        dash_heuristic_health_caps: "HEURISTIC HEALTH",
        dash_active_threats: "Active Threats",
        dash_active_threats_caps: "ACTIVE THREATS",
        dash_sensor_load: "Sensor Load",
        dash_sensor_load_caps: "SENSOR LOAD",
        dash_honeypot_nodes: "Honeypot Nodes",
        dash_honeypot_nodes_caps: "HONEYPOT NODES",
        dash_active: "ACTIVE",
        dash_normal: "NORMAL",
        dash_nodes_sync: "12 nodes synchronized globally",
        dash_no_anomalies: "No anomalies detected in last 24h",
        
        // Scanner (Exact matches)
        scan_title: "Scanner",
        scan_intel: "Automated Intelligence",
        tab_raw: "RAW INPUT",
        tab_direct: "Direct Input",
        tab_file: "File Upload",
        label_email_source: "EMAIL SOURCE CODE",
        label_header_analysis: "Header Analysis",
        btn_execute_scan: "Execute Scan",
        btn_execute_forensic: "Execute Forensic Scan",
        placeholder_headers: "Paste full email headers here for forensic analysis...",
        placeholder_source: "Paste raw email headers and body here...",
        
        // Documentation
        doc_hero_title: "Master the Clinical Sentinel.",
        doc_kb: "Knowledge Base",
        doc_get_started: "Get Started",
        doc_signal_title: "Signal Decryption",
        doc_sandbox_title: "Behavioral Sandboxing",
        
        // Support
        sup_concierge: "Concierge Support",
        sup_hero_title: "How can we secure your flow?",
        sup_label_name: "Identity Name",
        sup_label_email: "Secure Email",
        sup_btn_init: "Initialize Support Request",
        
        // General
        btn_login: "Log In",
        btn_signup: "Sign up for free",
        status_live: "SYSTEM LIVE",
        status_blocked: "Threats Blocked",
        last_verified: "Last verified 2 hours ago by Sentinel Core Team.",
        login_welcome: "Welcome Back",
        login_subtitle: "Authenticate to access the Sentinel Dashboard.",
        login_email_label: "Email Address",
        login_pwd_label: "Password",
        real_time_intel: "Real-Time Intelligence"
    },
    es: {
        // Navigation
        nav_security_scan: "Escaneo de Seguridad",
        nav_full_scanner: "Escáner Completo",
        nav_threat_feed: "Feed de Amenazas",
        nav_scan_history: "Historial de Escaneo",
        nav_security_vault: "Bóveda de Seguridad",
        nav_data_reports: "Informes de Datos",
        nav_account: "Cuenta",
        nav_documentation: "Documentación",
        nav_support: "Soporte",
        nav_new_scan: "Nuevo Escaneo",
        
        // Dashboard
        dash_title: "Inspección Profunda",
        dash_subtitle: "Análisis heurístico avanzado para la protección de correo crítico.",
        dash_engine_status: "Estado del Motor",
        dash_optimal_security: "Seguridad Óptima",
        dash_heuristic_health: "Salud Heurística",
        dash_heuristic_health_caps: "SALUD HEURÍSTICA",
        dash_active_threats: "Amenazas Activas",
        dash_active_threats_caps: "AMENAZAS ACTIVAS",
        dash_sensor_load: "Carga del Sensor",
        dash_sensor_load_caps: "CARGA DEL SENSOR",
        dash_honeypot_nodes: "Nodos Honeypot",
        dash_honeypot_nodes_caps: "NODOS HONEYPOT",
        dash_active: "ACTIVO",
        dash_normal: "NORMAL",
        dash_nodes_sync: "12 nodos sincronizados globalmente",
        dash_no_anomalies: "No se detectaron anomalías en las últimas 24h",
        
        // Scanner
        scan_title: "Escáner",
        scan_intel: "Inteligencia Automatizada",
        tab_raw: "ENTRADA SIN PROCESAR",
        tab_direct: "Entrada Directa",
        tab_file: "Carga de Archivo",
        label_email_source: "CÓDIGO FUENTE DEL CORREO",
        label_header_analysis: "Análisis de Encabezados",
        btn_execute_scan: "Ejecutar Escaneo",
        btn_execute_forensic: "Ejecutar Escaneo Forense",
        placeholder_headers: "Pegue los encabezados de correo aquí para el análisis forense...",
        placeholder_source: "Pegue los encabezados y el cuerpo del correo aquí...",
        
        // Documentation
        doc_hero_title: "Domine el Clinical Sentinel.",
        doc_kb: "Base de Conocimientos",
        doc_get_started: "Empezar",
        doc_signal_title: "Descifrado de Señales",
        doc_sandbox_title: "Sandboxing de Comportamiento",
        
        // Support
        sup_concierge: "Soporte Concierge",
        sup_hero_title: "¿Cómo podemos asegurar su flujo?",
        sup_label_name: "Nombre de Identidad",
        sup_label_email: "Correo Seguro",
        sup_btn_init: "Inicializar Solicitud de Soporte",
        
        // General
        btn_login: "Iniciar Sesión",
        btn_signup: "Regístrese gratis",
        status_live: "SISTEMA EN VIVO",
        status_blocked: "Amenazas Bloqueadas",
        last_verified: "Verificado hace 2 horas por el equipo central.",
        login_welcome: "Bienvenido de Vuelta",
        login_subtitle: "Autentíquese para acceder al Panel Sentinel.",
        login_email_label: "Correo Electrónico",
        login_pwd_label: "Contraseña",
        real_time_intel: "Inteligencia en Tiempo Real"
    }
};

function updateLanguage(lang) {
    document.documentElement.lang = lang;
    localStorage.setItem('preferred_lang', lang);
    
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (translations[lang] && translations[lang][key]) {
            el.innerText = translations[lang][key];
        }
    });

    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
        const key = el.getAttribute('data-i18n-placeholder');
        if (translations[lang] && translations[lang][key]) {
            el.placeholder = translations[lang][key];
        }
    });

    document.querySelectorAll('[data-lang]').forEach(btn => {
        if (btn.getAttribute('data-lang') === lang) {
            btn.classList.add('bg-primary', 'text-white');
            btn.classList.remove('text-primary', 'bg-transparent');
        } else {
            btn.classList.remove('bg-primary', 'text-white');
            btn.classList.add('text-primary', 'bg-transparent');
        }
    });
}

document.addEventListener('DOMContentLoaded', () => {
    const savedLang = localStorage.getItem('preferred_lang') || 'en';
    updateLanguage(savedLang);
});
