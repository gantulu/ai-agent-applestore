def valid_output():
    return {
        "template_version": "1.0.0",
        "brand": {
            "project_name": "Draft project", "market": "MY", "platform": "instagram",
            "content_locale": "en-MY", "affiliation_statement": "Draft disclaimer"
        },
        "request": {
            "topic": "iPhone Focus modes", "objective": "education", "audience": "Apple users",
            "primary_category": {"category_id": "CAT-007", "category_slug": "tips", "category_name": "Tips"},
            "secondary_category": None, "request_summary": "A practical Focus modes tip."
        },
        "product": {
            "product_name": "iPhone", "model": None, "generation": None, "configuration": None,
            "evidence": []
        },
        "creative": {
            "concept": "A calm, focused daily routine", "content_angle": "Practical iPhone tip",
            "key_message": "Make Focus work around your day.",
            "visual_style": {
                "mood": ["calm", "minimal"], "palette": ["soft white", "graphite"],
                "lighting": "Soft natural light", "composition": "Single focal point",
                "typography": "Clean sans-serif", "graphic_elements": ["subtle labels"]
            },
            "image_prompt": "Create a premium, accurate iPhone lifestyle visual in portrait composition.",
            "negative_prompt": "No distorted device, fake UI, inaccurate logos, or watermark."
        },
        "copywriting": {
            "headline": "Make space for focus", "subheadline": None,
            "body_copy": "Set a Focus mode that fits your routine.",
            "caption": "A calmer way to organise your day. Explore Focus settings on your iPhone.",
            "cta": "Explore Focus settings", "hashtags": ["#iPhone", "#AppleTips"]
        },
        "format_specification": {
            "format_id": "single_image", "placement": "instagram_feed", "aspect_ratio": "4:5",
            "generation_canvas": {"width_px": 2048, "height_px": 2560, "profile_id": "portrait_2k_long_edge_2560"},
            "export_canvas": {"width_px": 1080, "height_px": 1350}, "safe_area": "Keep key content away from edges."
        },
        "assets": {"required_assets": ["Accurate iPhone product reference"], "reference_assets": [], "usage_rights_status": "not_required"},
        "compliance": {
            "source_verification_status": "not_required", "brand_affiliation_checked": False,
            "asset_rights_status": "not_required", "factual_claims": [], "warnings": [],
            "human_review_required": True
        },
        "quality_control": {
            "status": "review_ready", "schema_validation": "pending",
            "checks": {
                "category_format": True, "locale": True, "generation_dimensions": True,
                "factual_claims": True, "brand_safety": True, "asset_rights": True
            },
            "human_approval_required": True
        }
    }
