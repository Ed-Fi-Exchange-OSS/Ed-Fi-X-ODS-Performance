from edfi_performance.api.client import EdFiAPIClient
from edfi_performance.api.client.school import SchoolClient


class CourseClient(EdFiAPIClient):
    endpoint = 'courses'


class CourseTranscriptClient(EdFiAPIClient):
    endpoint = 'courseTranscripts'

    dependencies = {
        'edfi_performance.api.client.student.StudentAcademicRecordClient': {
            'client_name': 'record_client',
        }
    }

    def create_with_dependencies(self, **kwargs):
        school_id = kwargs.pop('schoolId', SchoolClient.shared_elementary_school_id())

        record_reference = self.record_client.create_with_dependencies(schoolId=school_id)

        # Create course transcript
        return self.create_using_dependencies(
            record_reference,
            courseReference__educationOrganizationId=school_id,
            studentAcademicRecordReference__educationOrganizationId=school_id,
            studentAcademicRecordReference__studentUniqueId=record_reference['attributes']['studentReference']
            ['studentUniqueId'],
            **kwargs
        )