import factory

from edfi_performance.api.client.school import SchoolClient
from edfi_performance.factories import APIFactory
from edfi_performance.factories.descriptors.utils import build_descriptor
from edfi_performance.factories.utils import current_year, formatted_date


class GradeFactory(APIFactory):
    gradeTypeDescriptor = build_descriptor('GradeType', 'Grading Period')
    letterGradeEarned = "B"
    numericGradeEarned = 80
    gradingPeriodReference = factory.Dict(
        dict(
            schoolId=SchoolClient.shared_elementary_school_id(),
            gradingPeriodDescriptor=build_descriptor('GradingPeriod', 'First Six Weeks'),
            periodSequence=1,
            schoolYear=current_year(),
        )
    )
    studentSectionAssociationReference = factory.Dict(
        dict(
            beginDate=formatted_date(8, 23),
            localCourseCode='ELA-01',
            schoolId=SchoolClient.shared_elementary_school_id(),
            schoolYear=current_year(),
            studentUniqueId=1111111,  # Default value for scenarios, but not in DB
            sessionName="2016-2017 Fall Semester",
            sectionIdentifier="ELA012017RM555",
        )
    )
