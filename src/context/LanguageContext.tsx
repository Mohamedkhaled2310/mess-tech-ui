'use client';

import React, { createContext, useContext, useState, useEffect } from 'react';
import { Locale, Direction } from '@/types';
import { translations } from '@/i18n/translations';

interface LanguageContextType {
  locale: Locale;
  dir: Direction;
  toggleLanguage: () => void;
  setLocale: (locale: Locale) => void;
  t: (key: keyof typeof translations['ar']) => string;
}

const LanguageContext = createContext<LanguageContextType | undefined>(undefined);

export function LanguageProvider({ children }: { children: React.ReactNode }) {
  const [locale, setLocaleState] = useState<Locale>('ar');

  useEffect(() => {
    // Check saved preference or default to Arabic
    const saved = localStorage.getItem('mess_locale') as Locale;
    if (saved === 'ar' || saved === 'en') {
      setLocaleState(saved);
      document.documentElement.lang = saved;
      document.documentElement.dir = saved === 'ar' ? 'rtl' : 'ltr';
    } else {
      document.documentElement.lang = 'ar';
      document.documentElement.dir = 'rtl';
    }
  }, []);

  const setLocale = (newLocale: Locale) => {
    setLocaleState(newLocale);
    localStorage.setItem('mess_locale', newLocale);
    document.documentElement.lang = newLocale;
    document.documentElement.dir = newLocale === 'ar' ? 'rtl' : 'ltr';
  };

  const toggleLanguage = () => {
    const next = locale === 'ar' ? 'en' : 'ar';
    setLocale(next);
  };

  const t = (key: keyof typeof translations['ar']): string => {
    return translations[locale][key] || translations['ar'][key] || String(key);
  };

  const dir: Direction = locale === 'ar' ? 'rtl' : 'ltr';

  return (
    <LanguageContext.Provider value={{ locale, dir, toggleLanguage, setLocale, t }}>
      {children}
    </LanguageContext.Provider>
  );
}

export function useLanguage() {
  const context = useContext(LanguageContext);
  if (!context) {
    throw new Error('useLanguage must be used within a LanguageProvider');
  }
  return context;
}
