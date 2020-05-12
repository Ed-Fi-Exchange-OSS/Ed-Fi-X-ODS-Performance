import factory

from edfi_performance.api.client.school import SchoolClient
from .. import APIFactory
from ..descriptors.utils import build_descriptor
from ..utils import UniquePrimaryKeyAttribute


class GradingPeriodFactory(APIFactory):
    periodSequence = UniquePrimaryKeyAttribute()
    beginDate = "2014-08-23"
    endDate = "2014-10-04"
    totalInstructionalDays = 29
    schoolReference = factory.Dict(dict(schoolId=SchoolClient.shared_elementary_school_id()))
    schoolYearTypeReference = factory.Dict(dict(schoolYear=2014))
    gradingPeriodDescriptor = build_descriptor("GradingPeriod", "First Six Weeks")
