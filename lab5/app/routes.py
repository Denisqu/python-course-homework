from fastapi import FastAPI, APIRouter, status
from .main import app
from . import schemas, model
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from .database import get_db


# retrieve all tests
@app.get("/api/tests")
def get_tests(db: Session = Depends(get_db)):
    tests = db.query(model.Test).all()
    return {"tests": tests}


# add a new test
@app.post("/api/tests", status_code=status.HTTP_201_CREATED)
def post_test(payload: schemas.TestSchema, db: Session = Depends(get_db)):
    _new_test = model.Test(**payload.dict())
    db.add(_new_test)
    db.commit()
    db.refresh(_new_test)
    return {"status":"success", "note": _new_test}



# get a single test
@app.get("/api/tests/{test_id}")
def get_single_test(test_id: int, db: Session = Depends(get_db)):
    _test = db.query(model.Test).filter(model.Test.id == test_id).first()

    if not _test:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No test with this id: {test_id} found')

    return {"status":"success", "test":_test}


# edit a test
@app.patch("/api/tests/{testId}")
def edit_test(test_id: int, payload: schemas.TestSchema, db: Session = Depends(get_db)):
    _test_q = db.query(model.Test).filter(model.Test.id == test_id)
    _test = _test_q.first()
    if not _test:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No test with this id: {id} found')

    update_data = payload.dict(exclude_unset=True)
    _test_q.filter(model.Test.id == test_id).update(update_data,
                                                    synchronize_session=str(False))
    db.commit()
    db.refresh(_test)
    return {"status": "success", "test": _test}


# remove a test
@app.delete("/api/tests/{testId}")
def delete_test(test_id: int, db: Session = Depends(get_db)):
    _test_q = db.query(model.Test).filter(model.Test.id == test_id)
    _test = _test_q.first()
    if not _test:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No test with this id: {id} found')
    _test_q.delete(synchronize_session=str(False))
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)