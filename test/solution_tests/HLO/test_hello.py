from lib.solutions.HLO import hello_solution



class TestHello():
    def test_hello_world(self):
        assert hello_solution.hello(friend_name="Hello world.") == "Hello world."
