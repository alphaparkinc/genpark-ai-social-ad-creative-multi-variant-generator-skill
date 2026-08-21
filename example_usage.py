from client import AiSocialAdCreativeMultiVariantGeneratorClient

def main():
    client = AiSocialAdCreativeMultiVariantGeneratorClient()
    res = client.generate_variants("AI workflow automation platform for ops teams", "B2B SaaS founders", "LinkedIn")
    print(f"Estimated CTR: {res['estimated_ctr_pct']}%")
    print(f"Recommended: [{res['recommended_variant']['style']}] {res['recommended_variant']['headline']}")
    print("All Variants:")
    for v in res["ad_variants"]:
        print(f"  {v['id']} [{v['style']}]: {v['headline']} | CTA: {v['cta']}")

if __name__ == "__main__":
    main()
