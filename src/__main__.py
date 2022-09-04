# If you are using PyCharm as your ide be sure to run `pre-commit run --all-files` before commiting
# Because PyCharm dosen't have a Pre-Commit hook.
from src.world import World


if __name__ == "__main__":
    world = World()
    world.run()
