from typing import Optional
from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import HTMLResponse

from backend.models.schemas import LegalNoticeDocument
from backend.services.incident_manager import incident_manager

router = APIRouter(tags=["Legal Notices & Documents"])


@router.get("/api/v1/events/{event_id}/notice", response_model=LegalNoticeDocument, summary="Generate Legal Notice Dossier")
@router.get("/api/events/{event_id}/notice", response_model=LegalNoticeDocument, include_in_schema=False)
async def get_legal_notice(event_id: str, format: Optional[str] = Query("json", description="json or html")):
    """
    Generates a formal legal regulatory enforcement notice dossier under the
    Air (Prevention and Control of Pollution) Act, 1981 for the given event ID.
    Supports printable HTML output or structured JSON payload.
    """
    notice = incident_manager.generate_legal_notice(event_id)
    if not notice:
        raise HTTPException(status_code=404, detail=f"Environmental Event {event_id} not found for notice generation")
        
    if format and format.lower() == "html":
        return HTMLResponse(content=notice.html_document, status_code=200)
        
    return notice
