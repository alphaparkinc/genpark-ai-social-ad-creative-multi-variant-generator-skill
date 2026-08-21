class AiSocialAdCreativeMultiVariantGeneratorClient:
    def generate_variants(self, product_description: str, target_audience: str = "SaaS founders", ad_platform: str = "LinkedIn") -> dict:
        variants = [
            {"id": "V1", "headline": "Stop losing deals to slow follow-up", "body": f"AI-powered {ad_platform} ads that close 3x faster. Built for {target_audience}.", "cta": "Get Free Demo", "style": "Pain-Point"},
            {"id": "V2", "headline": "Your competitors are already using AI ads", "body": f"Don\'t get left behind. Generate 50 high-converting ad variants in 60 seconds.", "cta": "Try Free Today", "style": "FOMO"},
            {"id": "V3", "headline": "From brief to live ad in 60 seconds", "body": f"Trusted by 12,000+ growth teams. No design skills needed.", "cta": "Start Free", "style": "Speed-Proof"}
        ]
        return {"ad_variants": variants, "recommended_variant": variants[0], "estimated_ctr_pct": 4.7}
