class DjangoDBRouter:
    route_app_labels = {"admin", "auth", "contenttypes", "sessions"}
    db_name = "django"

    def db_for_read(self, model, **hints):
        """
        Attempts to read dashboard models go to public.
        """
        if model._meta.app_label in self.route_app_labels:
            return self.db_name
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write dashboard models go to public.
        """
        if model._meta.app_label in self.route_app_labels:
            return self.db_name
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the django apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the django apps only appear in the
        'public' database.
        """
        if app_label in self.route_app_labels:
            return db == self.db_name
        return None



class DashboardRouter:
    route_app_labels = {"dashboard"}
    db_name = "surveydb"

    def db_for_read(self, model, **hints):
        """
        Attempts to read dashboard models go to surveydb.
        """
        if model._meta.app_label in self.route_app_labels:
            return self.db_name
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write dashboard models go to surveydb.
        """
        if model._meta.app_label in self.route_app_labels:
            return self.db_name
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the django apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the dashboard app only appear in the
        'surveydb' database.
        """
        if app_label in self.route_app_labels:
            return db == self.db_name
        return None


class AlertsRouter:
    route_app_labels = {"alerts"}
    db_name = "alerts"

    def db_for_read(self, model, **hints):
        """
        Attempts to read alerts models go to alerts database.
        """
        if model._meta.app_label in self.route_app_labels:
            return self.db_name
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write alerts models go to alerts database.
        """
        if model._meta.app_label in self.route_app_labels:
            return self.db_name
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the django apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the alerts app only appear in the
        alerts database.
        """
        if app_label in self.route_app_labels:
            return db == self.db_name
        return None
