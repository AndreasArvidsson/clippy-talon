from talon import app, registry

required_captures = [
    "number_small",
    "user.letter",
    "user.number_key",
    "user.ordinals_small",
    "user.prose",
]


required_actions = [
    "sleep",
    "edit.paste",
    "user.rpc_client_run_command",
]


def on_ready():
    missing_captures = [
        capture for capture in required_captures if capture not in registry.captures
    ]
    missing_actions = [
        action for action in required_actions if action not in registry.actions
    ]
    errors = []
    if missing_captures:
        errors.append(f"Missing captures: {', '.join(missing_captures)}")

    if missing_actions:
        errors.append(f"Missing actions: {', '.join(missing_actions)}")
    if errors:
        print("\n".join(errors))
        app.notify(
            "Please install the community repository",
            body="https://github.com/talonhub/community",
        )


app.register("ready", on_ready)
