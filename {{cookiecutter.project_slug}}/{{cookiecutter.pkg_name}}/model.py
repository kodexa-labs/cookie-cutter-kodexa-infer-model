"""Main module."""

from kodexa import Document, get_source, PipelineContext, KodexaClient, Assistant
from kodexa.platform.client import ProjectEndpoint, DocumentFamilyEndpoint
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def infer(document: Document, project_endpoint: ProjectEndpoint, document_family_endpoint: DocumentFamilyEndpoint, client: KodexaClient, pipeline_context: PipelineContext, assistant: Assistant):

    logger.info(f"Infer called with document: {document.uuid}")

    logger.info(f"Project: {project_endpoint.name}")
    logger.info(f"Document Family: {document_family_endpoint.path}")

    # Lets see if we have extracted any data
    logger.info("Extracted Data:")
    logger.info(document_family_endpoint.get_json(project_id=project_endpoint.project_id, include_exceptions=True, inline_audits=True))

    # Lets add a label to the document
    document.add_label("my_first_model")

    # Lets download the native document (the source PDF or file)
    with get_source(document) as native_source:
        # Load document directly from bytes
        source_bytes: bytes = native_source.read()
        logger.info(f"Source Bytes: {len(source_bytes)}")

    # We also have a client configured
    logger.info(f"Client: {client.get_platform()}")

    # We can also get the pipeline context
    logger.info(f"Pipeline Context: {pipeline_context}")

    # We can also get the assistant
    logger.info(f"Assistant: {assistant}")

    return document
