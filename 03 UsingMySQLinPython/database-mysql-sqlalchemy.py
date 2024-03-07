## Building a model with SQLAlchemy ORM
import sqlalchemy
from sqlalchemy import Column, String, Integer, create_engine, ForeignKey, select
from sqlalchemy.orm import registry, relationship, Session


user = "root"
password = "MySQL123"
db_name = "projects"

engine = sqlalchemy.create_engine(f'mysql+mysqlconnector://{user}:{password}@localhost:3306/{db_name}',
                                  echo=True)
# print(f'mysql+mysqlconnector://{user}:{password}@localhost:3306/{db_name}')

mapper_registry = registry()
# mapper_registry.metadata

Base = mapper_registry.generate_base()

class Project(Base):
    __tablename__ = 'projects'
    project_id = Column(Integer, primary_key=True)
    title = Column(String(length=50))
    description = Column(String(length=255))

    def __repr__(self):
        # return "<Project(title='{0}', description='{1}')>".format(self.title, self.description)
        return f"<Project(title={self.title}, description={self.description})>"

class Task(Base):
    __tablename__ = 'tasks'
    task_id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.project_id'))
    description = Column(String(length=255))

    project = relationship("Project")

    def __repr__(self):
        return f"<Task(description={self.description})"

Base.metadata.create_all(engine)

# ### Adding data to the database using SQLAlchemy Sessions
# ## Sessions are how we create transactios with SQLAlchemy. Transcations are set of all or none queries
# with Session(engine) as session:
#     organize_closet_project = Project(title="Organize closet", 
#                                       description="Organize closet by color and style")
    
#     session.add(organize_closet_project)

#     session.flush()

#     tasks = [
#         Task(project_id=organize_closet_project.project_id, 
#              description="Decide what clothes to donate"),
#         Task(project_id=organize_closet_project.project_id,
#              description="Organize summer clothes"),
#         Task(project_id=organize_closet_project.project_id, 
#              description="Organize winter clothes")
#     ]

#     session.bulk_save_objects(tasks)

#     session.commit()

#### Retrieving data using SQLAlchemy ORM
with Session(engine) as session:
    smt = select(Project).where(Project.title == 'Organize closet')
    results = session.execute(smt)
    organize_closet_project = results.scalar()

    smt = select(Task).where(Task.project_id == organize_closet_project.project_id)
    results = session.execute(smt)
    for task in results:
        print(task)


