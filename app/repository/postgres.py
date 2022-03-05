from sqlmodel import select, Session, desc


class PostgresRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_last_contest(self, model):
        with self.session as session:
            result = session.exec(select(model.concurso).order_by(desc(model.concurso))).first()
            return result

    def get_all(self, model, offset: int, limit: int):
        with self.session as session:
            results = session.exec(select(model).limit(limit).offset(offset).order_by(desc(model.concurso))).all()
            return results

    def get_by_id(self, id, model):
        with self.session as session:
            result = session.exec(select(model).where(model.id == id)).first()
            return result

    def save(self, model):
        with self.session as session:
            session.add(model)
            session.commit()
            session.refresh(model)

        return model

    def save_all(self, model):
        with self.session as session:
            session.add_all(model)
            session.commit()
            # session.refresh(model)

        return

    def get_by_game(self, game, model):
        with self.session as session:
            return session.exec(select(model).where(model.concurso == game)).all()
