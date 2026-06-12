from fastapi.testclient import TestClient

from src.app import app, activities


client = TestClient(app)


def test_unregister_participant_removes_student_from_activity():
    activity_name = "Chess Club"
    email = "michael@mergington.edu"

    # Ensure the participant is present before the test.
    assert email in activities[activity_name]["participants"]

    response = client.delete(f"/activities/{activity_name}/unregister?email={email}")

    assert response.status_code == 200
    assert email not in activities[activity_name]["participants"]
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"

    # Restore state for later tests.
    activities[activity_name]["participants"].append(email)
