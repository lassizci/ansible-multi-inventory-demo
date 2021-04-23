from ansible.plugins.inventory import BaseInventoryPlugin

class InventoryModule(BaseInventoryPlugin):
    NAME = "some"

    def verify_file(self, path):
        valid = False
        if super(InventoryModule, self).verify_file(path):
            if path.endswith('some.yml'):
                valid = True
        return valid

    def parse(self, inventory, loader, path, cache=True):
        super(InventoryModule, self).parse(inventory, loader, path, cache)

        for i in range(1,5):
            hostname = f"some-host{i}.domain"
            self.inventory.add_host(hostname)
            self.inventory.set_variable(hostname, "inventory_source", "some")
