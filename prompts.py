

RESUME_PROMPTS = {
	"Summary": """This are the introduction about summary section which you are going to rewrite for user who is applying for specific job.
            
            Choose a title for this section that reflects who user is and how he want to represent himself.
            
            Goal: This key section provides a concise overview of your qualifications, showing the employer, in a few short seconds, how user stand out from other candidates. You may draw qualifications from any area of user's life (e.g., work, volunteer experience, education, or other activities). Typically, include four to six (maximum seven) points outlining users relevant strengths and achievements, beginning with the most relevant to the job. Points may begin with nouns or adjectives. Describe users competitive advantage — the value user offer.
            
            Goal: Tailor Summary of Qualifications section (and résumé) according to Job Description. Keep this section precise and accurate wording.
            
            Goal: Summary section must be industry specific. However, rather than copy sentences from a Job Description, include key words commonly used in the industry (Job Description) to which you are applying. No need to include all the keywords just a few to keep it natural.
            
            Highlight any key or unique achievements that will help user stand out among other applicants. Use strong adjectives and facts to describe users strengths. A phrase such as “Two years’ experience completing projects in…” has more impact than “good knowledge of …” Include following bullet points:

            1. As a first bullet (if applicable), users experience (from paid/unpaid work, academics, or extracurricular activities) relevant to the position sought (e.g., one year experience in graphic design; three years process engineering experience with key responsibilities in product design and implementation; solid academic career focusing on business development initiatives in the field of specialty catalysts)
            2. Users relevant knowledge/skills/expertise (e.g., “computer proficiency, report writing, program planning, public speaking, problem-solving”)
            3. Any education that complements users practical experience (e.g., “machine design, resource assessment, marketing”)
            4. A general reference to where user developed the skill (e.g., “proven leadership skills developed through three summers as camp counsellor”). Include this level of detail only once or twice so that points do not become too lengthy
            5. Personal characteristics and attributes; however, include only those that are relevant to the position user is seeking and if it aligns with the job description (e.g., consistently able to deliver results under tight deadlines vs punctual, honest, etc.)
            6. Specialized training/education if completed by user otherwise it should not be mentioned (e.g., “CPR certification”)

            Rewrite just the user summary section along with job discription provided with all the above Goal in check and follow instructions provided in the above list if applicable.
            Your response should be in form of paragraph
	""",
	"Experience":"""
	""",
	"Projects":"""
	""",
}

ASSESS_PROMPTS =  """You are an experienced recruiter writer with over 10 years of experience.
					This is Summary section of the resume rate it from scale of 1-10 and also provide some feedback to imporve the resume if available.
					Critize wherever possible
					"""
