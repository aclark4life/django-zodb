# django_zodb/management/commands/runzeo.py

from django.core.management.base import BaseCommand
import ZEO
import ZODB
import transaction


class Command(BaseCommand):
    help = "Run ZEO server with in-memory storage in the foreground"

    def handle(self, *args, **kwargs):
        # Start a ZEO server with dynamic address and in-memory storage
        address, stop = ZEO.server()

        self.stdout.write(self.style.SUCCESS(f"Starting ZEO server on {address[0]}:{address[1]}..."))

        # Create a ZEO client connection
        client_storage = ZEO.client(address)
        db = ZODB.DB(client_storage)
        connection = db.open()

        # Access the root of the database
        root = connection.root()
        # You can perform operations here, for example:
        # root['example_key'] = 'example_value'
        # transaction.commit()  # Uncomment to commit changes

        try:
            # Keep the server running in the foreground
            while True:
                # Optional: Print a message or status every few seconds
                self.stdout.write(self.style.SUCCESS("ZEO server is running... Press Ctrl+C to stop."))
                import time
                time.sleep(10)  # Adjust the sleep duration as needed
        except KeyboardInterrupt:
            self.stdout.write(self.style.WARNING("ZEO server stopped."))

        finally:
            # Clean up and close connections properly
            connection.close()
            db.close()
            stop()  # Call stop to shut down the ZEO server
