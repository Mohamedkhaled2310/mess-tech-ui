import { clsx, type ClassValue } from 'clsx';
import { twMerge } from 'tailwind-merge';

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export function formatPrice(price: number, locale: 'ar' | 'en' = 'ar'): string {
  const formatted = price.toLocaleString(locale === 'ar' ? 'ar-EG' : 'en-US');
  const currency = locale === 'ar' ? 'ج.م' : 'EGP';
  return locale === 'ar' ? `${formatted} ${currency}` : `${currency} ${formatted}`;
}
