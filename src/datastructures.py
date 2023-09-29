
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        self._members = []

        # Inicializo la familia con los tres miembros especificados
        self.add_member({
            "first_name": "John",
            "age": 33,
            "lucky_numbers": [7, 13, 22]
        })
        self.add_member({
            "first_name": "Jane",
            "age": 35,
            "lucky_numbers": [10, 14, 3]
        })
        self.add_member({
            "first_name": "Jimmy",
            "age": 5,
            "lucky_numbers": [1]
        })

    def get_all_members(self):
        return self._members








    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

   
    def add_member(self, member):
        if "id" not in member:
            member["id"] = self._generateId()

        self._members.append(member)


    def delete_member(self, id):
        for member in self._members:
            if member.get("id") == id:
                self._members.remove(member)
                return True

        return False

    def get_member(self, member_id):
        for member in self._members:
            if member["id"] == member_id:
                return {
                    "id": member["id"],
                    "first_name": member["first_name"],
                    "age": member["age"],
                    "lucky_numbers": member["lucky_numbers"]
                }

        return None



