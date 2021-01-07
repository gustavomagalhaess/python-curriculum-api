from flask_restful import Resource
from resources.resource import Resource as ResourceHelper, check_json, list_map, list_map_curriculum
from models.segment import SegmentModel
from models.resume import ResumeModel
from models.graduation import GraduationModel
from models.certification import CertificationModel
from models.skill import SkillModel
from models.company import CompanyModel
from models.product import ProductModel
from models.presentation import PresentationModel

class Curriculum(Resource, ResourceHelper):
    
    def __init__(self):
        super().__init__(None)

    def get(self, segment_id):
        resume = ResumeModel.get_current_by_segment(segment_id)
        graduations = GraduationModel.get_all_by_segment(segment_id, True)
        certifications = CertificationModel.get_all_by_segment(segment_id)
        skills = SkillModel.get_all_by_segment(segment_id)
        companies = CompanyModel.get_all_by_segment(segment_id, True)
        products = ProductModel.get_all_by_segment(segment_id)
        presentations = PresentationModel.get_all_by_segment(segment_id, True)

        return {
            'curriculum': 
                {
                    'resume': check_json(resume),
                    'graduations': list_map(graduations),
                    'certifications': list_map_curriculum(certifications),
                    'skills': list_map_curriculum(skills),
                    'companies': list_map_curriculum(companies),
                    'products': list_map_curriculum(products),
                    'presentations': list_map_curriculum(presentations)

                }
        }, 200