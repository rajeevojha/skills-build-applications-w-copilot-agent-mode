import logging
from bson import ObjectId
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from pprint import pprint

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        logger.debug('Starting database population script.')

        # Clear existing data
        logger.debug('Clearing existing data from collections.')
        User.objects.filter(id__isnull=False).delete()
        Team.objects.filter(id__isnull=False).delete()
        Activity.objects.filter(id__isnull=False).delete()
        Leaderboard.objects.filter(id__isnull=False).delete()
        Workout.objects.filter(id__isnull=False).delete()

        logger.debug('Existing data cleared.')

        # Add test users
        logger.debug('Adding test users.')
        user1 = User.objects.create(id=ObjectId(), email="user1@example.com", name="User One", password="password1")
        logger.debug(f'User created: {user1}')
        user2 = User.objects.create(id=ObjectId(), email="user2@example.com", name="User Two", password="password2")
        logger.debug(f'User created: {user2}')

        # Add test teams
        logger.debug('Adding test teams.')
        team1 = Team.objects.create(id=ObjectId(), name="Team Alpha", members=[user1.id, user2.id])
        logger.debug(f'Team created: {team1}')

        # Add test activities
        logger.debug('Adding test activities.')
        Activity.objects.create(id=ObjectId(), user=user1, activity_type="Running", duration=30)
        logger.debug('Activity created for user1: Running, 30 minutes')
        Activity.objects.create(id=ObjectId(), user=user2, activity_type="Cycling", duration=45)
        logger.debug('Activity created for user2: Cycling, 45 minutes')

        # Add test leaderboard
        logger.debug('Adding test leaderboard.')
        Leaderboard.objects.create(id=ObjectId(), team=team1, score=100)
        logger.debug('Leaderboard entry created for team1: Score 100')

        # Add test workouts
        logger.debug('Adding test workouts.')
        Workout.objects.create(id=ObjectId(), name="Push Ups", description="Do 20 push ups")
        logger.debug('Workout created: Push Ups')
        Workout.objects.create(id=ObjectId(), name="Squats", description="Do 15 squats")
        logger.debug('Workout created: Squats')

        logger.debug('Database population script completed successfully. Added test data for')
        self.stdout.write(self.style.SUCCESS('Database populated with test data for'))

        # Function to find and pretty print one user and one workout
        def find_and_print_one_user_and_workout():
            user = User.objects.first()
            workout = Workout.objects.first()

            if user:
                logger.debug('Found one user:')
                pprint(vars(user))
            else:
                logger.debug('No users found in octofit_tracker_user.')

            if workout:
                logger.debug('Found one workout:')
                pprint(vars(workout))
            else:
                logger.debug('No workouts found in octofit_tracker_workout.')

        # Call the function at the end of the script
        find_and_print_one_user_and_workout()
