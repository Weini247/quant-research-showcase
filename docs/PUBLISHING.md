# Publication and maintenance

This is the **public, curated** Quant Research Lab showcase associated with [Weini247](https://github.com/Weini247).

## Website

The static site is already stored in `index.html`. To serve it using GitHub Pages:

1. Open repository **Settings → Pages**.
2. Under **Build and deployment**, choose **Deploy from a branch**.
3. Select branch `main`, directory `/(root)`, and save.
4. Once Pages reports a successful deployment, the expected public URL is `https://weini247.github.io/quant-research-showcase/`.

The page uses no analytics, credentials, trading API or live data.

## Local verification

Run from repository root:

```bash
python examples/synthetic_accounting/demo.py
python -m unittest discover -s examples/synthetic_accounting -p 'test_*.py' -v
```

The Python demonstration uses fictional securities and exact decimal arithmetic. GitHub Actions is configured to repeat its automated tests.

## Update discipline

- Review the public disclosure policy before every release.
- Publish no private research code, proprietary signals, licensed raw market data or credentials.
- Clearly distinguish designed components, implemented demonstrations and validated empirical results.
- Do not state that a trading strategy is profitable or deployed without independent evidence.
- Screen ENNEAD screenshots for filenames, user identifiers, account details and research secrets.

## Optional GitHub profile README

Copy `profile/README.md` to the root of a separate public `Weini247/Weini247` repository when you're ready to present an account-level portfolio. This step is **not** completed by this showcase publication.
