



# @pytest_asyncio.fixture(scope="session")
# async def mongodb_client():
#     """
#     Set up a test database for the session.
#     """
#     # Use a test database URI
#     test_db_uri = "mongodb://127.0.0.1:27017/?replicaSet=rs0"
#     client = AsyncIOMotorClient(test_db_uri)
#     client.get_io_loop = asyncio.get_event_loop
#     database_name = "test"
#     db = client.get_database(database_name)

#     await init_beanie(
#         database=db,
#         document_models=[
#             User,
#         ],
#     )

#     app.state.mongo_client = client

#     yield client

#     await client.drop_database(database_name)


# @pytest_asyncio.fixture(scope="function", autouse=True)
# async def clear_collections(mongodb_client):
#     """
#     Clear all collections before each test.
#     Don't clear pre-populated collections from migrations: capture_tasks, health_areas, biomarkers
#     """
#     for model in [User]:
#         await model.get_motor_collection().delete_many({})
#     yield
