# $FreeBSD$

PORTNAME=	home-assistant
DISTVERSION=	0.113.3
CATEGORIES=	sysutils python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	y@trombik.org
COMMENT=	Open source home automation that puts local control and privacy first

LICENSE=	APACHE20
LICENSE_FILE=	${WRKSRC}/LICENSE.md

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}aiohttp>0:www/py-aiohttp \
	${PYTHON_PKGNAMEPREFIX}astral>0:devel/py-astral \
	${PYTHON_PKGNAMEPREFIX}async_timeout>0:devel/py-async_timeout \
	${PYTHON_PKGNAMEPREFIX}attrs>0:devel/py-attrs \
	${PYTHON_PKGNAMEPREFIX}bcrypt>0:security/py-bcrypt \
	${PYTHON_PKGNAMEPREFIX}certifi>0:security/py-certifi \
	${PYTHON_PKGNAMEPREFIX}ciso8601>0:textproc/py-ciso8601 \
	${PYTHON_PKGNAMEPREFIX}cryptography>0:security/py-cryptography \
	${PYTHON_PKGNAMEPREFIX}importlib-metadata>0:devel/py-importlib-metadata \
	${PYTHON_PKGNAMEPREFIX}Jinja2>0:devel/py-Jinja2 \
	${PYTHON_PKGNAMEPREFIX}pyjwt>0:www/py-pyjwt \
	${PYTHON_PKGNAMEPREFIX}pip>0:devel/py-pip \
	${PYTHON_PKGNAMEPREFIX}pytz>0:devel/py-pytz \
	${PYTHON_PKGNAMEPREFIX}requests>0:www/py-requests \
	${PYTHON_PKGNAMEPREFIX}ruamel.yaml>0:textproc/py-ruamel.yaml \
	${PYTHON_PKGNAMEPREFIX}python-slugify>0:textproc/py-python-slugify \
	${PYTHON_PKGNAMEPREFIX}voluptuous>0:devel/py-voluptuous \
	${PYTHON_PKGNAMEPREFIX}voluptuous-serialize>0:devel/py-voluptuous-serialize \
	${PYTHON_PKGNAMEPREFIX}yarl>0:www/py-yarl

USES=		python:3.7+
USE_PYTHON=	autoplist distutils

USE_GITHUB=	yes
GH_TUPLE=	home-assistant:core:${DISTVERSION}
NO_ARCH=	yes

pre-configure:
	${REINPLACE_CMD} 's/==/>=/g' \
		${WRKSRC}/setup.py ${WRKSRC}/homeassistant/package_constraints.txt

.include <bsd.port.mk>
