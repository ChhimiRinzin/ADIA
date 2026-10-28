import streamlit as st
from sqlalchemy.exc import SQLAlchemyError
from config import DATABASE_URL
from recovery import fetch_summary, format_nu, make_engine

st.set_page_config(page_title='ADIA | Audit Recovery', page_icon='📊', layout='centered')
st.title('Audit Recovery Dashboard')
st.caption('ADIA • Version 1 — Total Recovered')
st.info('Demo data only unless connected to an authorized read-only database.')

if st.button('Refresh total', type='primary'):
    st.rerun()

try:
    engine = make_engine(DATABASE_URL)
    try:
        summary = fetch_summary(engine)
    finally:
        engine.dispose()
    st.metric('Total Recovered Amount', format_nu(summary.total))
    st.caption(f'Based on {summary.payment_count:,} posted payment records. Pending and void records are excluded.')
    st.caption('Definition of posted and treatment of reversals must be verified before production use.')
except SQLAlchemyError:
    st.error('Could not retrieve recovery data. Check database connectivity, permissions and approved table mapping.')
except Exception:
    st.error('The recovery summary could not be displayed. Contact the system administrator.')
