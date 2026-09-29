import unittest
import todo


class TodoTests(unittest.TestCase):
    def test_add_assigns_incrementing_ids(self):
        tasks = []
        todo.add_task(tasks, "first")
        second = todo.add_task(tasks, "second")
        self.assertEqual(second["id"], 2)

    def test_complete_task(self):
        tasks = []
        todo.add_task(tasks, "write tests")
        self.assertTrue(todo.complete_task(tasks, 1))
        self.assertTrue(tasks[0]["done"])
        self.assertFalse(todo.complete_task(tasks, 99))

    def test_remove_task(self):
        tasks = []
        todo.add_task(tasks, "temp")
        self.assertTrue(todo.remove_task(tasks, 1))
        self.assertEqual(tasks, [])
        self.assertFalse(todo.remove_task(tasks, 1))


if __name__ == "__main__":
    unittest.main()
