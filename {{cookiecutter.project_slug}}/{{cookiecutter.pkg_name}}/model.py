"""Main module."""

from kodexa import Document
from kodexa.platform.client import ProjectEndpoint, DocumentFamilyEndpoint
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def infer(document: Document, project_endpoint: ProjectEndpoint, document_family_endpoint: DocumentFamilyEndpoint):
    logger.info(f"Infer called with document: {document.uuid}")

    logger.info(f"Project: {project_endpoint.name}")
    logger.info(f"Document Family: {document_family_endpoint.path}")

    # Lets see if we have extracted any data
    logger.info("Extracted Data:")
    logger.info(document_family_endpoint.get_json(project_id=project_endpoint.project_id, include_exceptions=True, inline_audits=True))

    # Lets add a label to the document
    document.add_label("my_first_model")

    return document
