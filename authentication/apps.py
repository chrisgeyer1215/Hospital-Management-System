from django.apps import AppConfig

class AppointmentsConfig(AppConfig):
    name = 'appointments'

    def ready(self):
        # Import signals to connect them
        import appointments.signals
