# import pytest

# from src.models import User


# @pytest.mark.asyncio
# async def test_user():
#     inserted_user = await User(name="name").insert()

#     fetched_user = await User.find_one(User.name == "name")

#     assert inserted_user == fetched_user
