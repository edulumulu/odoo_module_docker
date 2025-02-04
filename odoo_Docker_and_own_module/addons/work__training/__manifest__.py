{
    'name': 'Work Training',
    'version': '1.0',
    'summary': 'Gestión de las acciones formativas de la empresa para los empleados.',
    'description': """
       Módulo para la gestión de programas de formación de empleados:
            - Acciones formativas con formadores y participantes.
            - Integración con empleados de RRHH y partners.
            - Cálculo de sesiones en función de la duración del curso y horas de sesión.
    """,
    'author': 'Eduardo Lucas',
    'website': '',
    'category': 'Human Resources',
    'depends': ['base', 'hr', 'contacts'],  # Añadimos dependencias clave
    'data': [
        'security/ir.model.access.csv',
        'views/course_views.xml',
        'views/trainer_views.xml',
        'views/session_views.xml',
        'report/training_report.xml',
        'views/training_template.xml',
        'report/training_report_2.xml',
        'views/training_template_2.xml',
        'views/employee_views.xml', 
        'views/partner_views.xml',
        
        
    ],
    
    'installable': True,
    'application': True,
}
