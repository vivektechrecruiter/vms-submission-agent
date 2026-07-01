def format_employment_history(employment_history):

    experience_text = ""

    for job in employment_history:

        company = job.get("company", "")
        location = job.get("location", "")
        start_date = job.get("start_date", "")
        end_date = job.get("end_date", "")
        title = job.get("title", "")

        experience_text += (
            f"{company}, {location}\t\t{start_date} - {end_date}\n"
        )

        experience_text += f"{title}\n\n"

        experience_text += "Responsibilities:\n"

        for responsibility in job.get(
            "responsibilities", []
        ):
            experience_text += (
                f"• {responsibility}\n"
            )

        subsections = job.get(
            "subsections", []
        )

        if subsections:

            experience_text += "\n"

            for subsection in subsections:

                experience_text += (
                    f"{subsection.get('name', '')}:\n"
                )

                for responsibility in subsection.get(
                    "responsibilities", []
                ):
                    experience_text += (
                        f"• {responsibility}\n"
                    )

                experience_text += "\n"

        experience_text += "\n"

    return experience_text


def build_resume_context(candidate_data):

    return {
        "candidate_name": candidate_data.get(
            "candidate_name", ""
        ),

        "location": candidate_data.get(
            "location", ""
        ),

        "professional_summary": "\n\n".join(
            candidate_data.get(
                "professional_summary", []
            )
        ),

        "skills_summary": "\n".join(
            candidate_data.get(
                "skills_summary", []
            )
        ),

        "employment_history": format_employment_history(
            candidate_data.get(
                "employment_history", []
            )
        ),

        "education": "\n".join(
            candidate_data.get(
                "education", []
            )
        ),

        "certifications": "\n".join(
            candidate_data.get(
                "certifications", []
            )
        )
    }