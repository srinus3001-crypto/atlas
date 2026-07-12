from atlas.core.runtime import RuntimeContext
from atlas.core.runtime import EnterpriseRuntime


class FakeEmployee:
    def execute(self, context):
        return {"status": "success", "employee": context.employee}


ctx = RuntimeContext(
    workspace_id="P001",
    employee="FakeEmployee",
    department="Testing",
    title="Runtime Test",
)

runtime = EnterpriseRuntime()

result = runtime.execute(ctx, FakeEmployee())

print(result)
