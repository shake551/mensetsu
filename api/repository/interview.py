from sqlalchemy.orm import Session

import api.models.interview as interview_model
import api.schemas.interview as interview_schema


def create_interview(
        db: Session, interview_create: interview_schema.InterviewCreate, user_id: int = 1
) -> interview_model.Interview:
    interview = interview_model.Interview(**interview_create.dict(), send_by=user_id)

    db.add(interview)
    db.commit()
    db.refresh(interview)

    return interview
