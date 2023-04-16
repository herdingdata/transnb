from transnb.commands import get_mastodon_api


def test__can_see_mastodon():
    # basically do we have valid settings configured and credentials which work?
    api = get_mastodon_api()
    result = api.verify_credentials()

    assert result.screen_name == "transnb"
