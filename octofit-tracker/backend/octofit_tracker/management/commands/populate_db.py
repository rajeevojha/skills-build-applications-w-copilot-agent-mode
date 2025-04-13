from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Add test users
        user1 = User.objects.create(email="user1@example.com", name="User One", password="password1")
        user2 = User.objects.create(email="user2@example.com", name="User Two", password="password2")

        # Add test teams
        team1 = Team.objects.create(name="Team Alpha", members=[user1.id, user2.id])

        # Add test activities
        Activity.objects.create(user=user1, activity_type="Running", duration=30)
        Activity.objects.create(user=user2, activity_type="Cycling", duration=45)

        # Add test leaderboard
        Leaderboard.objects.create(team=team1, score=100)

        # Add test workouts
        Workout.objects.create(name="Push Ups", description="Do 20 push ups")
        Workout.objects.create(name="Squats", description="Do 15 squats")

        self.stdout.write(self.style.SUCCESS('Database populated with test data'))
