
"""

Execution Engine



Coordinates execution across multiple Atlas offices.

"""



from atlas.core.logger import Logger

from atlas.offices.office_registry import OfficeRegistry

from atlas.knowledge.memory import MemoryRepository





class ExecutionEngine:



    def __init__(self):



        self.registry = OfficeRegistry()

        self.memory = MemoryRepository()



    def execute(self, mission):



        Logger.info(

            f"Execution Engine received mission {mission.mission_id}"

        )



        current_office = mission.owner_office



        last_result = None



        while current_office:



            office = self.registry.get(current_office)



            if office is None:



                Logger.error(

                    f"Office '{current_office}' not found"

                )



                break



            Logger.info(

                f"Executing Office : {current_office}"

            )



            result = office.execute(mission)



            Logger.info(

                f"Office Result : {result.status}"

            )



            self.memory.save(result)



            last_result = result



            current_office = result.next_office



            if current_office:



                Logger.info(

                    f"Routing Mission -> {current_office}"

                )



        Logger.info("Mission Workflow Completed")



        return last_result



